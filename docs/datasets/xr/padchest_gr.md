# PadChest-GR (Grounded Report Generation)

PadChest-GR (Castro et al., NEJM AI 2025; Microsoft Research +
Universidad de Alicante + BIMCV) is the first manually curated dataset
designed specifically to train grounded radiology report generation
(GRRG) models. It is a 4,555-study subset derived from the parent
PadChest corpus (160k images), with substantially deeper structured
annotation.

Composition:
- 4,555 chest-radiograph studies (1,456 normal, 3,099 abnormal).
- 7,037 positive finding sentences + 3,422 negative finding sentences,
  each in both English and Spanish - making this the only large
  bilingual grounded-RRG benchmark.
- Up to two independent sets of bounding boxes per positive finding
  sentence, drawn by 14 radiologists.
- Categorical labels per finding for type, locations, and progression.

Pipeline: GPT-4 (Microsoft Azure OpenAI Service) was used to extract
single-finding sentences from the original PadChest reports, translate
them between Spanish and English, link them to the existing PadChest
finding/location label set, and classify finding progression. The 14
radiologists then discarded poor-quality studies and manually
annotated the bounding boxes.

This is the strongest current open benchmark for evaluating
grounded-RRG models such as MAIRA-2, RaDialog, and CheXagent. It
should be paired with PadChest (parent corpus, 160k images) and
Open-i / IU CXR (English-only RRG benchmark) for full coverage of
the report-generation task spectrum.

Distribution: HuggingFace mirror at StanfordAIMI/padchest-gr;
canonical access via the BIMCV PadChest portal under the PadChest
Research Use Agreement. Approximate size is ~5 GB.

DOI: https://doi.org/10.1056/AIdbp2401120
