"""Extract frames from echocardiography videos (.avi/.mp4) to .npy or .jpg with optional resize."""

from __future__ import annotations

import sys
from pathlib import Path

import click


def _try_import_decord():
    try:
        import decord  # type: ignore
        return decord
    except ImportError:
        return None


def _try_import_cv2():
    try:
        import cv2  # type: ignore
        return cv2
    except ImportError:
        return None


def _try_import_numpy():
    try:
        import numpy as np  # type: ignore
        return np
    except ImportError as e:
        raise SystemExit("missing tool: install numpy (pip install numpy)") from e


def _resize_frame(frame, size, np, cv2):
    if size is None:
        return frame
    if cv2 is not None:
        return cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    # Pure-numpy nearest-neighbor fallback.
    h_new, w_new = size[1], size[0]
    h, w = frame.shape[:2]
    yi = (np.linspace(0, h - 1, h_new)).astype(np.int64)
    xi = (np.linspace(0, w - 1, w_new)).astype(np.int64)
    return frame[yi[:, None], xi[None, :]]


def _save_frame(frame, path: Path, fmt: str, np, cv2) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "npy":
        np.save(str(path.with_suffix(".npy")), frame)
        return
    if cv2 is None:
        raise SystemExit("missing tool: install opencv-python to write .jpg (pip install opencv-python)")
    cv2.imwrite(str(path.with_suffix(".jpg")), frame)


def _decord_extract(video: Path, out_dir: Path, target_fps: float, size, fmt: str, decord, np, cv2):
    vr = decord.VideoReader(str(video))
    src_fps = float(vr.get_avg_fps()) or 30.0
    step = max(1, int(round(src_fps / max(target_fps, 1e-6))))
    indices = list(range(0, len(vr), step))
    n = 0
    for i in indices:
        frame = vr[i].asnumpy()
        frame = _resize_frame(frame, size, np, cv2)
        _save_frame(frame, out_dir / f"{video.stem}_{i:06d}", fmt, np, cv2)
        n += 1
    return n


def _cv2_extract(video: Path, out_dir: Path, target_fps: float, size, fmt: str, cv2, np):
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise SystemExit(f"error: cannot open video: {video}")
    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    step = max(1, int(round(src_fps / max(target_fps, 1e-6))))
    n = 0
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % step == 0:
            frame = _resize_frame(frame, size, np, cv2)
            _save_frame(frame, out_dir / f"{video.stem}_{idx:06d}", fmt, np, cv2)
            n += 1
        idx += 1
    cap.release()
    return n


@click.command()
@click.option(
    "--in",
    "in_path",
    "in_path",
    required=True,
    type=click.Path(exists=True),
    help="Input video file or directory of videos.",
)
@click.option("--out", "out_dir", required=True, type=click.Path(file_okay=False))
@click.option("--fps", "target_fps", type=float, default=15.0, show_default=True)
@click.option("--size", default=None, help="Resize WxH e.g. 224x224 (omit for native).")
@click.option(
    "--fmt", "fmt", type=click.Choice(["jpg", "npy"]), default="jpg", show_default=True
)
def main(in_path: str, out_dir: str, target_fps: float, size: str | None, fmt: str) -> None:
    np = _try_import_numpy()
    decord = _try_import_decord()
    cv2 = _try_import_cv2()
    if decord is None and cv2 is None:
        raise SystemExit(
            "missing tool: install decord (pip install decord) or opencv-python (pip install opencv-python)"
        )

    parsed_size = None
    if size:
        try:
            w, h = (int(x) for x in size.lower().split("x"))
            parsed_size = (w, h)
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"error: --size must be WxH (got {size!r})") from e

    in_path_p = Path(in_path)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    if in_path_p.is_file():
        videos = [in_path_p]
    else:
        videos = [
            p for p in in_path_p.rglob("*") if p.suffix.lower() in {".avi", ".mp4", ".mov", ".mkv"}
        ]

    total = 0
    for v in videos:
        sub_out = out_path / v.stem
        if decord is not None:
            n = _decord_extract(v, sub_out, target_fps, parsed_size, fmt, decord, np, cv2)
        else:
            n = _cv2_extract(v, sub_out, target_fps, parsed_size, fmt, cv2, np)
        click.echo(f"ok: {v.name} -> {n} frames")
        total += n

    click.echo(f"ok: total {total} frames across {len(videos)} videos")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        click.echo(f"error: {e}", err=True)
        sys.exit(1)
