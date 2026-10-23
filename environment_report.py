"""Print a reproducibility-oriented software/hardware environment report."""
import platform
import sys

print("Python:", sys.version.replace("\n", " "))
print("Platform:", platform.platform())

packages = [
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("Pillow", "PIL"),
    ("opencv-python", "cv2"),
    ("scikit-learn", "sklearn"),
    ("matplotlib", "matplotlib"),
    ("tqdm", "tqdm"),
    ("timm", "timm"),
    ("torch", "torch"),
    ("torchvision", "torchvision"),
]

print("\nPackage versions:")
for label, module_name in packages:
    try:
        module = __import__(module_name)
        version = getattr(module, "__version__", "version not exposed")
        print(f"{label}: {version}")
    except Exception as exc:
        print(f"{label}: NOT AVAILABLE ({exc})")

try:
    import torch
    print("\nPyTorch/CUDA:")
    print("torch CUDA build:", torch.version.cuda)
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU count:", torch.cuda.device_count())
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}:", torch.cuda.get_device_name(i))
        print("cuDNN:", torch.backends.cudnn.version())
except Exception as exc:
    print("\nPyTorch/CUDA report unavailable:", exc)
