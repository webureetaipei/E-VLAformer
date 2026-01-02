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
curl -fsSL [https://get.docker.com](https://get.docker.com) -o get-docker.sh
sudo sh get-docker.sh
sudo apt-get install -y nvidia-container-toolkit

# 2. Pull Isaac Sim Image
docker pull nvcr.io/nvidia/isaac-sim:4.2.0

# 3. Run Container (Headless Mode with Streaming)
docker run --name isaac-sim --entrypoint bash -it --gpus all -e "ACCEPT_EULA=Y" --rm --network=host nvcr.io/nvidia/isaac-sim:4.2.0