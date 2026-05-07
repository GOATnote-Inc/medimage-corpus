# M4Raw (Low-Field 0.3T Brain k-space)

M4Raw is the first publicly available raw k-space MRI dataset from a 0.3T low-field whole-body MRI system, providing critical infrastructure for reconstruction research targeting accessible point-of-care MRI (Hyperfine, Promaxo, etc.). The dataset contains multi-channel brain k-space from 183 healthy volunteers covering T1-weighted, T2-weighted, and FLAIR sequences at ~1.2 mm in-plane / 5 mm through-plane resolution. Each contrast includes multiple repetitions usable individually or as multi-repetition averaged ground truth. After motion-corruption exclusion, partitioned splits contain 1024 training and 240 validation volumes.

## Access and tier

Open. Hosted on Zenodo (DOI: 10.5281/zenodo.7523691). Click-through; no application.

## Format and download

Native: HDF5 raw k-space, multi-channel. Recommended: HDF5 direct ingestion with parallel-imaging or denoising-aware unrolled networks. Companion code at https://github.com/mylyu/M4Raw.

## Intended use for this corpus

Reconstruction, denoising, and parallel-imaging research targeting low-field MRI. Bridges the high-field-only fastMRI corpus to accessible 0.3T-and-below systems. Critical for democratizing MRI in LMIC and rural settings.

## License

CC BY 4.0.

## Reference

Lyu M et al., "M4Raw: A multi-contrast, multi-repetition, multi-channel MRI k-space dataset for low-field MRI research." Sci Data 10, 264 (2023). DOI: 10.1038/s41597-023-02181-4
