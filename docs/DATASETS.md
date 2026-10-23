# Dataset acquisition and licensing

The ultrasound datasets used in this study are **not redistributed** in this repository. Download each dataset from its original public source and comply with the terms shown by the provider at the time of access.

## 1. CUBS — Carotid Ultrasound Boundary Study

- Source: Mendeley Data, Version 1
- DOI: https://doi.org/10.17632/fpv535fss7.1
- Dataset page: https://data.mendeley.com/datasets/fpv535fss7/1
- Licence: **CC BY 4.0**
- Study use: 2,176 B-mode images. The definitive pipeline performs a participant-level 80/10/10 split (1,740/218/218); only the 1,740 training images enter SSL. Manual-A1 LI and MA annotations are used to construct the grayscale proxy target. The LI–MA wall polygon was successfully constructed for all 2,176 CUBS images; the rectangle and centre-crop fallback branches present in the preprocessing code were not used for the analysed dataset.

The Mendeley record describes the dataset as containing the image dataset, clinical parameters, manual segmentations and computerized segmentations associated with the CUBS study.

## 2. Orvile — Carotid Ultrasound Images

- Source: Kaggle, dataset owner `orvile`
- Dataset page: https://www.kaggle.com/datasets/orvile/carotid-ultrasound-images
- Study use: 1,100 accepted B-mode images are included in the SSL pool. The definitive pipeline recursively identifies image files and excludes paths indicative of masks, segmentations, ground truth or labels.
- Licence/terms: **verify the current licence/usage terms displayed on the Kaggle dataset page before downloading or redistributing the data.** The public source could be verified during repository preparation, but the dataset licence was not reliably exposed through the available metadata, so no licence is asserted here.

This repository does not redistribute Orvile images or masks.

## 3. Ar-PlaqSegm1 — First Argentine database of B-mode ultrasound images for atherosclerotic plaque segmentation

- Source: Mendeley Data, Version 2
- DOI: https://doi.org/10.17632/8srkpz52dy.2
- Dataset page: https://data.mendeley.com/datasets/8srkpz52dy/2
- Licence: **CC BY 4.0**
- Study use: the supplied dataset contains 493 training pairs and 48 test pairs. The definitive pipeline makes a fixed 80/20 split of the supplied training set, giving 394 training, 99 validation and 48 test image-mask pairs. The supplied 48-image test set is retained unchanged.

The dataset publication reports 541 image-mask pairs in total and a 48-image test set containing 24 plaque-positive and 24 plaque-negative images.

## Redistribution policy

No source ultrasound images, masks or clinical data from these datasets are included in this repository. This repository contains code and small derived experimental result files only. Users are responsible for obtaining the source datasets and following their respective licences and platform terms.

## Expected local data

The definitive notebooks preserve the Google Drive paths used for the study. After downloading the datasets, either reproduce the expected directory structure or edit the path/configuration cells near the beginning of each notebook. See `REPRODUCIBILITY.md` for the execution order.
