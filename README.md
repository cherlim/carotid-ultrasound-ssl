# Self-supervised representation learning for carotid B-mode ultrasound

Reproducibility package for a study evaluating whether carotid-domain self-supervised adaptation improves ViT-S/16 representations relative to ImageNet initialization. The study evaluates **representation learning and transfer**, not clinical diagnostic performance.

## Study overview

An ImageNet-pretrained ViT-S/16 is adapted using 2,840 unlabelled carotid B-mode images from CUBS and Orvile. Two SSL approaches are evaluated:

1. **EMA-based latent self-distillation inspired by I-JEPA** — online encoder, predictor and EMA target encoder; both encoders process the complete augmented image and 20% of patch positions are selected after encoding for the latent prediction objective.
2. **MAE-style masked reconstruction** — a 75% masking reconstruction control using the same ViT-S/16 backbone, ImageNet initialization, SSL image pool and 15-epoch training budget.

Downstream evaluation comprises frozen proxy classification (Experiment A), frozen plaque segmentation (Experiment B1), and supervised fine-tuning (Experiment B2).

## Repository contents

```text
notebooks/
  01_ssl_ema_and_mae_adaptation.ipynb
  02_experiment_A_frozen_classification.ipynb
  03_experiment_B1_frozen_segmentation.ipynb
  04_experiment_B2_finetuning.ipynb
  05_figure_CUBS_proxy_distribution.ipynb
  06_figure_SSL_training_curves.ipynb
results/
  experiment_A/
  experiment_B1/
  experiment_B2/
  ssl_training/
docs/
  DATASETS.md
  ENVIRONMENT.md
  REPRODUCIBILITY.md
  MANUSCRIPT_TRACEABILITY.md
  REPOSITORY_AUDIT.md
  original_notebook_hashes.txt
environment_report.py
requirements.txt
```

## Data

The datasets are **not redistributed in this repository**. Authoritative acquisition information and licensing notes are provided in [`docs/DATASETS.md`](docs/DATASETS.md). In brief:

- **CUBS:** Mendeley Data, DOI `10.17632/fpv535fss7.1`, CC BY 4.0. Study split: 1,740/218/218 train/validation/test.
- **Orvile Carotid Ultrasound Images:** Kaggle dataset `orvile/carotid-ultrasound-images`. The current Kaggle licence/terms should be checked at access time; this repository does not assert a licence that could not be independently verified. Study SSL contribution: 1,100 accepted B-mode images.
- **Ar-PlaqSegm1:** Mendeley Data Version 2, DOI `10.17632/8srkpz52dy.2`, CC BY 4.0. Study split: 394/99/48 train/validation/test.

The SSL pool is 1,740 CUBS training images + 1,100 Orvile B-mode images = 2,840 images. The definitive notebooks retain the original Google Drive paths used for the study; update the path/configuration cells for your environment.

## Suggested reproduction order

1. Run `01_ssl_ema_and_mae_adaptation.ipynb` to construct the corrected SSL pool, CUBS proxy labels, and train the EMA-distillation and MAE-style encoders.
2. Run `02_experiment_A_frozen_classification.ipynb` for frozen CUBS proxy classification.
3. Run `03_experiment_B1_frozen_segmentation.ipynb` for frozen Ar-PlaqSegm1 segmentation and paired image-level analysis.
4. Run `04_experiment_B2_finetuning.ipynb` for supervised fine-tuning.
5. Use notebooks 05–06 for manuscript figure generation.

## Important terminology note

Some historical variable names and checkpoint filenames use `ijepa`. These names are retained inside the definitive notebooks to preserve provenance. The implemented method is **not canonical I-JEPA**; the manuscript describes it as EMA-based latent self-distillation inspired by I-JEPA.

## Results included

Small CSV files corresponding to the definitive runs are included under `results/`. Large datasets, caches, resume states and model checkpoints are excluded.

## Environment

The definitive experiments were run in Google Colab with PyTorch/timm. Exact historical package versions were not fully recorded, so the repository does not invent version pins. `requirements.txt` lists the verified principal dependencies, `docs/ENVIRONMENT.md` records the retained runtime/hardware evidence, and `environment_report.py` can be used to record the environment of a new reproduction run.

## Checkpoints

Study-trained `.pth` checkpoints are not distributed. Run Notebook 01 to regenerate the EMA-distillation and MAE-style encoders before running the downstream experiments. See `docs/REPRODUCIBILITY.md` for the execution sequence and expected reference results.

## Reproducibility documentation

See `docs/REPRODUCIBILITY.md` for design/provenance notes and `docs/MANUSCRIPT_TRACEABILITY.md` for the mapping between manuscript analyses and repository files.


## Repository audit

A public-release audit is included at `docs/REPOSITORY_AUDIT.md`. The definitive code/results pass the scientific traceability checks. Authoritative dataset acquisition/licensing information and the available environment provenance are documented. Study-trained checkpoints are intentionally not distributed; Notebook 01 regenerates them from the corrected 2,840-image SSL pool.

## Citation

A formal citation and DOI should be added here once the manuscript/preprint and archival repository record are available.


## Software environment

The definitive experiments were run in Google Colab. Exact historical package versions were not fully recorded, so the repository does not invent version pins. Verified dependencies are listed in `requirements.txt`; details of the retained hardware/runtime evidence and the recommended reproduction procedure are in `docs/ENVIRONMENT.md`. Run `environment_report.py` at the start of a new reproduction to record Python, package, PyTorch/CUDA, cuDNN and GPU information.
