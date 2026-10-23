# Repository audit report

**Audit date:** 2026-10-17  
**Scope:** definitive notebooks, included CSV outputs, repository documentation, and public-release hygiene.

## Overall assessment

**Status: scientifically traceable and prepared for v1.0 public release, pending creation of the public repository/archive URL.**

The definitive notebooks and included result CSVs are internally consistent with manuscript v07. No new numerical discrepancy was identified in Experiment A, Experiment B1, the B1 paired bootstrap analysis, or Experiment B2. The repository contains publication-cleaned versions of the definitive scientific notebooks; Markdown and comments were cleaned while executable scientific logic and stored outputs were preserved. A final documentation pass also verified that the LI–MA wall polygon was used for all 2,176 CUBS proxy values; the coded rectangle and centre-crop fallbacks were not invoked.

## Audit matrix

| Item | Status | Finding / action |
|---|---|---|
| Corrected SSL pool | PASS | Notebook 01 constructs 1,740 CUBS training B-mode + 1,100 Orvile B-mode images (2,840 total), excluding CUBS validation/test, Orvile mask-like paths, and Ar-PlaqSegm1 from SSL. |
| EMA-distillation implementation | PASS | ViT-S/16, ImageNet initialization, online/EMA-target encoders, predictor, 20% post-encoding patch-position selection, Smooth L1 loss, EMA 0.996, 15 epochs. |
| MAE-style implementation | PASS | ViT-S/16, ImageNet initialization, 75% random masking, learned mask token, lightweight decoder, masked-patch MSE, 15 epochs. |
| SSL augmentation reporting | PASS / NOTE | EMA and MAE use the same broad augmentation family but slightly different colour-jitter/grayscale settings. Repository documentation must not describe all augmentation parameters as matched. |
| Experiment A | PASS | Frozen encoders, linear head, 25/50/100% label fractions, seeds 42/43/44. Included CSV reproduces manuscript AUROC means. |
| Experiment B1 | PASS | Frozen encoders, segmentation decoder, 24 positive + 24 negative test images, seeds 42/43/44. Included summary reproduces manuscript Dice results. |
| B1 paired bootstrap | PASS | 24 positive images, seed-averaged image-level Dice, 100,000 paired bootstrap resamples. EMA vs ImageNet difference = +0.052569; 95% CI = +0.003302 to +0.100988. |
| Experiment B2 | PASS | ImageNet vs EMA initialization; encoder fine-tuned at 1e-5 and decoder at 1e-3; seeds 42/43/44. Included summary reproduces manuscript Dice results. |
| Figure 4B source | PASS / DEPENDENCY | Figure notebook correctly loads the processed CUBS cache and verifies n=1,740 and the saved median threshold, but the cache itself is not distributed. Independent users must first run Notebook 01. |
| Figure 8 source | PASS / FIXED IN DOCS | Figure notebook expects two CSVs in `/content/`. The repository already includes them under `results/ssl_training/`; documentation now states that users should upload/copy those files or edit the two paths. |
| Dataset acquisition | PASS / DOCUMENTED | `docs/DATASETS.md` records the authoritative CUBS and Ar-PlaqSegm1 Mendeley sources/DOIs and CC BY 4.0 licences, plus the authoritative Orvile Kaggle source. Because the Orvile licence was not independently exposed by available metadata, users are explicitly instructed to verify the current Kaggle licence/terms rather than relying on an unverified assertion. |
| Model checkpoints | DOCUMENTED | Study-trained `.pth` checkpoints are intentionally not distributed. Notebook 01 regenerates the EMA-distillation and MAE-style encoders from the corrected SSL pool. |
| Software environment | DOCUMENTED | Exact historical package versions were not preserved and are not guessed. `requirements.txt`, `docs/ENVIRONMENT.md`, and `environment_report.py` document the verified dependencies/evidence and the procedure for recording a new reproduction environment. |
| Hard-coded Drive paths | DOCUMENTED | Definitive notebooks contain original `/content/drive/MyDrive/...` paths. This preserves provenance but requires users to edit path/config cells. |
| Historical `IJEPA` names | DOCUMENTED | Internal variables/checkpoint names use `IJEPA_clean_2840`/`ijepa_...`. Documentation explicitly states this is historical naming for the EMA-based latent self-distillation implementation, not canonical I-JEPA. |
| Sensitive credentials | PASS | No API keys, passwords, email addresses, or authentication secrets were identified in the repository notebooks. An HF Hub warning mentioning `HF_TOKEN` is output text only, not a credential. |
| Large/private data | PASS | Ultrasound datasets, caches, resume states, and model checkpoints are not included. |
| CUBS proxy-region source | PASS / DOCUMENTED | Audit of the saved preprocessing cache showed wall = 2,176 (100%), rectangle = 0, centre-crop = 0. Documentation now records this explicitly. |

## Numerical spot checks

- Experiment A EMA mean AUROC: **0.8660 / 0.8760 / 0.8816** at 25% / 50% / 100% labels.
- Experiment A ImageNet mean AUROC: **0.8442 / 0.8582 / 0.8765**.
- Experiment B1 mean positive-case Dice: EMA **0.4086 ± 0.0217**; ImageNet **0.3560 ± 0.0332**.
- B1 EMA − ImageNet paired image-level Dice difference: **+0.052569**, 95% bootstrap CI **+0.003302 to +0.100988**.
- Experiment B2 mean positive-case Dice: EMA **0.4673 ± 0.0158**; ImageNet **0.3677 ± 0.0285**.

## Remaining release step

1. Create the public GitHub repository and/or archival record, then add its permanent URL/DOI to the README and manuscript Code Availability statement.

## Recommended but not scientifically required

- Add a single path-configuration cell or a short `config.example.py` for independent users. Do this only as a convenience layer; keep the definitive notebooks unchanged.
- Add a small script/notebook that regenerates manuscript summary tables directly from the included CSVs.

## Release decision

The repository is suitable as the **v1.0 reproducibility/provenance package**. No experimental rerun is indicated by this audit. The only remaining publication step is to create the public repository/archive location and add its permanent URL/DOI to the repository and manuscript.
