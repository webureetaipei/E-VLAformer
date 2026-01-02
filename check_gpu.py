import torch
import sys

print(f"✅ Python: {sys.version.split()[0]}")
print(f"✅ PyTorch: {torch.__version__}")
print(f"✅ CUDA Available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"🚀 GPU: {torch.cuda.get_device_name(0)}")
    x = torch.rand(5, 3).cuda()
    print(x)
else:
    print("❌ GPU NOT FOUND")