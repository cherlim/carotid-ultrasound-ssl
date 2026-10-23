# Manuscript-to-repository traceability

| Manuscript component | Repository source |
|---|---|
| SSL dataset construction, CUBS proxy labels, EMA-distillation adaptation, MAE-style adaptation | `notebooks/01_ssl_ema_and_mae_adaptation.ipynb` |
| Experiment A: frozen proxy classification | `notebooks/02_experiment_A_frozen_classification.ipynb`; `results/experiment_A/experiment_A_frozen_label_efficiency.csv` |
| Experiment B1: frozen plaque segmentation | `notebooks/03_experiment_B1_frozen_segmentation.ipynb`; `results/experiment_B1/experiment_B1_frozen_with_negative_analysis.csv` |
| B1 mean ± SD summary | `results/experiment_B1/experiment_B1_summary_mean_sd.csv` |
| B1 positive-case per-image analysis | `results/experiment_B1/experiment_B1_per_image_positive_cases.csv` |
| B1 paired bootstrap comparison | `results/experiment_B1/experiment_B1_paired_bootstrap.csv` |
| Experiment B2: supervised fine-tuning | `notebooks/04_experiment_B2_finetuning.ipynb`; `results/experiment_B2/experiment_B2_finetuning_results.csv` |
| B2 mean ± SD summary | `results/experiment_B2/experiment_B2_summary_mean_sd.csv` |
| CUBS proxy_raw histogram / Figure 4B source | `notebooks/05_figure_CUBS_proxy_distribution.ipynb` |
| SSL training curves / Figure 8 | `notebooks/06_figure_SSL_training_curves.ipynb`; `results/ssl_training/ema_distillation_history.csv`; `results/ssl_training/mae_style_history.csv` |
