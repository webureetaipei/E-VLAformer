# E-VLAformer: Neuro-Symbolic World Models for Robot Safety

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.5.1%2Bcu121-orange)
![Isaac Sim](https://img.shields.io/badge/NVIDIA-Isaac_Sim_4.2.0-green)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)

## 📅 Project Progress & Milestones (Development Log)

### Phase 1: Infrastructure & Environment (Current Focus)
This phase ensures the reproducibility of the Sim-to-Real environment on heterogeneous hardware (Windows/Linux hybrid).

- [x] **Task 01: System Infrastructure Setup**
  - Configured WSL2 (Ubuntu 20.04) on Windows 11.
  - Optimized NVIDIA Drivers (535+) for GPU Passthrough capability.
- [x] **Task 02: Simulation Environment Deployment**
  - Deployed NVIDIA Isaac Sim 4.2.0 via Docker Container.
  - Verified rendering and physics engine via Omniverse Streaming Client.
- [x] **Task 03: Deep Learning Runtime Setup**
  - Established isolated python environment via Miniconda.
  - Integrated PyTorch 2.5.1 with CUDA 12.1 support.
- [x] **Task 04: Development Environment Verification**
  - Configured VS Code Remote - WSL integration.
  - Validated GPU tensor operations (See `check_gpu.py`).
- [x] **Task 05: Project Structure Initialization** (In Progress)

### Phase 2: Core Implementation (Upcoming)
- [ ] VLA Model Integration (Transformer-based)
- [ ] Graph World Model Design
- [ ] Neuro-Symbolic Reasoning Pipeline

## 📖 Project Overview
This project implements a **Neuro-Symbolic VLA (Vision-Language-Action)** model integrated with a **Graph-based World Model** for enhanced robot safety in industrial environments. It features a distributed architecture and real-time **Sim-to-Real** deployment capability using NVIDIA Isaac Sim