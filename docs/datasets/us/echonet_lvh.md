# EchoNet-LVH

**Modality:** Ultrasound | **Anatomy:** Heart (left ventricle) | **View:** Parasternal long-axis (PLAX) | **Year:** 2022

## Overview
EchoNet-LVH is a Stanford-released dataset of 12,000 PLAX echocardiogram videos used to develop deep-learning models for left ventricular hypertrophy (LVH) detection and chamber-wall measurement. Unlike the smaller and aggressively downsampled EchoNet-Dynamic, LVH videos are stored at native resolution, which makes the dataset substantially larger (~75 GB estimated).

## Labels
Per-video clinical measurements: interventricular septum (IVS), left ventricular internal dimension (LVID), left ventricular posterior wall (LVPW) thickness in systole/diastole, plus categorical LVH etiology (cardiac amyloidosis, hypertrophic cardiomyopathy, hypertensive LVH, normal/other).

## Format
Native AVI, single-view PLAX. For training, recommend extracting MP4 + sampled frames into parquet so that throughput on H100/H200 nodes is bottlenecked by GPU rather than per-video AVI decode.

## Access
Stanford AIMI portal -- registration plus signed Research Use Agreement required (non-commercial). Downloadable from https://stanford.redivis.com/datasets/cchq-0srz1fy9a after agreement.

## Citation
Duffy et al., "High-throughput precision phenotyping of left ventricular hypertrophy with cardiovascular deep learning." *JAMA Cardiology* (2022). https://jamanetwork.com/journals/jamacardiology/fullarticle/2789370

## Notes for ingestion
- Largest single US dataset in this manifest by raw bytes.
- Pair with EchoNet-Dynamic for multi-view (PLAX + A4C) joint pretraining.
- Stanford EULA: re-host on local cluster only, no public model weights checkpoints derived without re-checking the agreement.
