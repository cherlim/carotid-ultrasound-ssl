# Reproducibility notes

## Scope
This repository packages the definitive Colab notebooks and small derived result files used for the manuscript. It does not redistribute the ultrasound datasets or model checkpoints.

## Dataset allocation
- CUBS: 2,176 images. Participant-level split: 1,740 train, 218 validation, 218 test. Only the 1,740 training images enter SSL adaptation. The Manual-A1 LI–MA wall polygon was successfully constructed for all 2,176 images when generating the grayscale proxy values; rectangle and centre-crop fallback branches were not used.
- Orvile: 1,100 accepted B-mode images enter SSL adaptation; mask/label-like paths are excluded by the definitive preprocessing notebook.
- Ar-PlaqSegm1: supplied training set is split into 394 train and 99 validation images; the supplied 48-image test set is retained for testing.

## SSL pool
The SSL pool contains 2,840 B-mode images: 1,740 CUBS training images + 1,100 Orvile images.

## Terminology
Historical code/checkpoint names contain `ijepa`. In the manuscript and repository documentation, the implemented method is described as **EMA-based latent self-distillation inspired by I-JEPA**, not canonical I-JEPA. Both online and EMA target encoders process the complete augmented image; 20% of patch positions are selected after encoding for the latent prediction objective.

## Definitive downstream design
- Experiment A: frozen encoders + linear classifier; label fractions 25%, 50%, 100%; seeds 42, 43, 44.
- Experiment B1: frozen encoders + segmentation decoder; seeds 42, 43, 44; positive-case segmentation metrics plus negative-case false-positive analysis.
- Experiment B1 paired analysis: per-image Dice averaged across three seeds, followed by 100,000 paired bootstrap resamples across 24 positive test images.
- Experiment B2: ImageNet vs EMA-distillation initialization with encoder fine-tuning; encoder LR 1e-5, decoder LR 1e-3; seeds 42, 43, 44.

## Paths
The supplied Colabs contain the original Google Drive paths used for the definitive runs. For independent reproduction, edit the configuration/path cells to point to local copies of the public datasets and a writable project directory. Scientific hyperparameters and analysis logic should remain unchanged.

## Checkpoints
Study-trained `.pth` checkpoints are intentionally not distributed. Run Notebook 01 to regenerate the EMA-distillation and MAE-style encoders before the downstream experiments.

## Expected reference results
These values are provided as checks that an independent run is following the intended analysis:
- Experiment A EMA mean AUROC: 0.8660, 0.8760, 0.8816 at 25%, 50%, 100% labels.
- Experiment B1 positive-case Dice: EMA 0.4086 ± 0.0217; ImageNet 0.3560 ± 0.0332.
- B1 paired EMA − ImageNet image-level Dice difference: +0.052569 (95% bootstrap CI +0.003302 to +0.100988).
- Experiment B2 positive-case Dice: EMA 0.4673 ± 0.0158; ImageNet 0.3677 ± 0.0285.

## Figure notebook dependencies
- `05_figure_CUBS_proxy_distribution.ipynb` loads the processed CUBS cache created by Notebook 01. Run Notebook 01 first or update `CACHE_PATH` to that cache.
- `06_figure_SSL_training_curves.ipynb` currently reads `/content/ssl_corrected_2840_history.csv` and `/content/mae_corrected_2840_history.csv`. Copies are included in `results/ssl_training/`; in Colab, upload/copy them to `/content/` or edit the two paths.

## Reproducibility caveat
The definitive notebooks preserve the original Google Drive paths and historical internal `IJEPA` labels. These are retained for provenance. Path edits needed for a new environment do not change the scientific configuration.
Because GPU training can involve nondeterministic operations, independently retrained checkpoints need not be bit-for-bit identical. Reproduction should therefore focus on the specified protocol, seeds, data construction and consistency with the reported downstream results rather than binary checkpoint identity.

## Public notebook documentation

The repository-facing notebooks retain the executable scientific code from the definitive experimental notebooks. Markdown headings and full-line explanatory comments were edited for clarity and to align terminology with the manuscript. Historical internal artifact names such as `IJEPA_clean_2840` remain where changing them could affect provenance or compatibility; these refer to the EMA-distillation condition described in the manuscript. An executable-code integrity check is recorded in `docs/original_notebook_hashes.txt`.



## Record the reproduction environment

Before running Notebook 01, install `requirements.txt` and run `environment_report.py`. Save its console output with the reproduction artifacts. The exact historical package versions were not preserved in the definitive notebooks; see `docs/ENVIRONMENT.md` for the verified environment information and rationale for leaving requirements unpinned.
