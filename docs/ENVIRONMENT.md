# Software and execution environment

## Scope

The definitive experiments were executed in Google Colab notebooks. The repository preserves the scientific code used for the reported analyses. Exact package-version output was not recorded in the definitive notebooks, so this repository does **not** claim exact historical version pins that cannot be verified.

## Verified software dependencies

The executable notebooks directly use the following Python packages:

- `torch`
- `torchvision`
- `timm`
- `numpy`
- `pandas`
- `scikit-learn`
- `Pillow`
- `opencv-python`
- `matplotlib`
- `tqdm`

These dependencies are listed in the repository `requirements.txt`. They are intentionally unpinned because the exact package versions used for the definitive runs were not recorded. Pinning guessed versions would give a false impression of provenance.

## Verified compute information

The definitive Experiment B1 and B2 notebook outputs record execution on CUDA with an **NVIDIA A100-SXM4-40GB** GPU. Notebook 01 also records CUDA execution, although the retained output does not identify the GPU model. Experiment A uses CUDA when available but its retained output does not preserve a GPU model/version record.

A CUDA-capable GPU is strongly recommended for SSL training and segmentation experiments. CPU execution is supported by portions of the code but is not the intended practical route for reproducing the complete study.

## Google Colab package installation

The definitive notebooks install only selected packages explicitly because core scientific packages are supplied by the Colab runtime. For example, the notebooks install `timm` and, where needed, `scikit-learn`, `pandas`, `tqdm`, `Pillow`, and `opencv-python`. PyTorch and torchvision are used from the runtime environment rather than being explicitly installed by the notebooks.

This is why `requirements.txt` describes the full Python dependency set rather than reproducing only the `pip install` lines in individual Colabs.

## Reproduction recommendation

For a new reproduction run:

1. Use a current Google Colab GPU runtime or an equivalent Linux/Python/CUDA environment.
2. Install the packages in `requirements.txt`.
3. Before training, run `python environment_report.py` (or execute its commands in Colab) and save the output with the reproduction artifacts.
4. Run the notebooks in the order described in `REPRODUCIBILITY.md`.
5. Compare generated summary CSVs with the reference CSVs under `results/` rather than expecting bit-for-bit identical model checkpoints.

## Why exact historical versions are not supplied

The definitive notebooks do not contain a complete `pip freeze`, Python version, CUDA toolkit version, cuDNN version, or exact versions for all imported packages. Some notebook outputs provide hardware information, but that is insufficient to reconstruct the complete historical environment reliably.

Accordingly, the repository distinguishes between:

- **verified information** preserved in the notebooks; and
- **recommended reproduction procedure** for future runs.

If an exact historical environment record is recovered later from the original Colab runtime metadata or a saved `pip freeze`, it can be added as a separate environment lock file without changing the scientific code.
