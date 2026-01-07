# Environment Setup Guide

## 1. Prerequisite: NVIDIA Driver & WSL2 (Task 01)
Before starting, ensure your Windows host meets the following requirements:
* **OS:** Windows 11 with WSL2 enabled (Ubuntu 20.04/22.04).
* **GPU:** NVIDIA RTX GPU (Driver version **535.xx** or later).
* **Networking:** Ensure WSL2 allows localhost connections.

## 2. Docker & Isaac Sim Installation (Task 02)
We utilize the official NVIDIA container for simulation.
```bash
# 1. Install Docker & NVIDIA Container Toolkit (WSL2)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo apt-get install -y nvidia-container-toolkit

# 2. Pull Isaac Sim Image
docker pull nvcr.io/nvidia/isaac-sim:4.2.0

# 3. Run Container (Headless Mode with Streaming)
docker run --name isaac-sim --entrypoint bash -it --gpus all -e "ACCEPT_EULA=Y" --rm --network=host nvcr.io/nvidia/isaac-sim:4.2.0
```

## 3. Python Environment Setup (Task 03)
We use Miniconda to manage the deep learning environment to avoid conflicts with the system Python.

### Step 1: Install Miniconda
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
source ~/miniconda3/bin/activate
```
### Step 2: Create Environment

Use the provided environment.yml for reproducibility:
```bash

# Create environment from file
conda env create -f environment.yml

# Activate environment
conda activate evlaformer
```

## 4. Verification (Task 04)
Run the diagnostic script to verify GPU visibility within WSL2.
```bash
# Activate environment
conda activate evlaformer

# Run check
python check_gpu.py
```
Expected Output:
✅ CUDA Available: True 🚀 GPU: NVIDIA GeForce RTX 4080 (or similar)

## 5. Project Structure Initialization (Task 05)
We establish a modular directory structure to separate simulation logic, model definition, and documentation. This ensures scalability as the codebase grows.

### Standard Directory Layout
Ensure your project root (`~/evlaformer`) follows this structure:

```text
evlaformer/
├── configs/        # Configuration files (YAML/JSON)
├── docs/           # Documentation (Setup guides, API docs)
├── src/            # Source code
│   ├── sim/        # Isaac Sim integration scripts
│   ├── vla/        # VLA Model architecture
│   └── utils/      # Helper functions
├── tests/          # Unit tests
├── .gitignore      # Git ignore rules
└── README.md       # Project overview
```

## 6. C++ Compilation Chain Setup (Task 06)

### Verify C++ Compilation Chain (Preparation for Phase 5)
Ensure GCC and CMake are available for future Custom Inference Engine development.
```bash
gcc --version   # Expected: gcc (Ubuntu 9.4.0+)
cmake --version # Expected: cmake version 3.x+
nvcc --version  # Expected: Cuda compilation tools
```