# 🧊 IceNav: Dynamic Path Planning for Complex Sea States

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python" />
  <img src="https://img.shields.io/badge/OS-Ubuntu%2020.04-orange?logo=ubuntu" />
  <img src="https://img.shields.io/badge/Planner-Lattice%20%2B%20A*-green" />
  <img src="https://img.shields.io/badge/Simulation-Pymunk%20%2B%20MSS-purple" />
  <img src="https://img.shields.io/badge/License-Academic%20Use-lightgrey" />
</p>

**IceNav** is a real-time local navigation system for autonomous vessels operating in broken ice fields.  
It is designed for sea states with **20%–50% ice concentration** and ice drift speeds up to **0.5 m/s**.

IceNav generates safe, smooth, and dynamically feasible paths while reducing collision risk and minimizing kinetic energy loss during ship–ice interactions.

---

## 📌 Table of Contents

- [✨ Highlights](#-highlights)
- [📊 Performance](#-performance)
- [🏗️ System Architecture](#️-system-architecture)
- [⚙️ Installation](#️-installation)
- [📦 Dependencies](#-dependencies)
- [🚀 Usage](#-usage)
- [🧪 Batch Experiments](#-batch-experiments)
- [📈 Evaluation](#-evaluation)
- [📁 Output](#-output)
- [🗂️ Project Structure](#️-project-structure)
- [📜 License](#-license)
- [📚 Citation](#-citation)
- [📬 Contact](#-contact)

---

## ✨ Highlights

### 🔄 Real-time Replanning

- Receding horizon strategy
- Lattice-based local planner
- Update cycle under **90 ms**
- Replanning frequency of **7–10 Hz**

### 🧊 Physics-based Collision Optimization

- 2D inelastic ship–ice collision model
- Minimizes kinetic energy loss
- Prioritizes avoiding:
  - Large ice blocks over **50 kg**
  - Head-on collisions with angles over **60°**

### 🚢 Ship Dynamics Constraints

- Minimum turning radius: **1.5 m**
- Maximum angular velocity: **0.5 rad/s**
- Maximum acceleration: **0.2 m/s²**

### 🧭 Two-stage Path Planning

- Improved A* for initial path generation
- Optimization refinement for smoother and safer trajectories

### 🧪 Integrated Simulation Framework

- Pymunk physics engine
- Marine Systems Simulator, MSS
- Trajectory visualization
- Performance evaluation

---

## 📊 Performance

Compared with the straight-line navigation method, IceNav achieves:

| Metric | Improvement |
|---|---:|
| 💥 Collisions | ↓ **61.3%** |
| ⚡ Energy loss | ↓ **59.1%** |
| 🎯 Position error | ↓ **31.8%** |

---

## 🏗️ System Architecture

```text
┌────────────────────┐
│ Perception Module  │
└─────────┬──────────┘
          ↓
┌────────────────────┐
│   Path Planning    │
└─────────┬──────────┘
          ↓
┌────────────────────────┐
│ Collision Optimization │
└─────────┬──────────────┘
          ↓
┌────────────────────┐
│ Simulation/Control │
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ Real-time Feedback │
└─────────┬──────────┘
          ↺
   Perception Module
```

---

## 🧩 Module Overview

### 👁️ Perception Module

The perception module provides a 2D environment model updated at **10 Hz**.

Supported input sources include:

- Camera
- Millimeter-wave radar
- IMU
- Pre-generated ice field datasets

---

### 🧭 Path Planning Module

The path planning module combines:

- Lattice planner
- Improved A*
- Embedded ship dynamics constraints

---

### 🧊 Collision Optimization Module

The collision optimization module uses a kinetic energy loss cost function with multi-objective weights:

| Objective | Weight |
|---|---:|
| 🛣️ Path length | 0.4 |
| 💥 Collision cost | 0.5 |
| 🧊 Ice concentration penalty | 0.1 |

---

### 🧪 Simulation Module

The simulation module is built with:

- Pymunk
- Marine Systems Simulator, MSS

It supports:

- Ship trajectory visualization
- Collision record analysis
- Performance evaluation

---

## ⚙️ Installation

### ✅ Requirements

- Python 3.9
- Linux, tested on Ubuntu 20.04

---

### 📥 Clone Repository

```bash
git clone https://github.com/yourusername/IceNav.git
cd IceNav
```

---

### 🐍 Create Conda Environment

```bash
conda create -n py39 python=3.9
conda activate py39
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🧊 Download Dataset

Download the ice field dataset and extract it to the `data/` directory.

Dataset information:

- **400** ice fields
- Approximately **500 MB**

Expected directory structure:

```text
IceNav/
└── data/
    └── ...
```

---

## 📦 Dependencies

Main dependencies include:

```text
casadi==3.6.5
decorator==5.1.1
fonttools==4.51.0
llvmlite==0.42.0
matplotlib==3.5.3
matplotlib-inline==0.1.6
mpld3==0.5.9
networkx==3.1
numba==0.59.1
numpy==1.26.4
opencv-python==4.9.0.80
packcircles==0.14
pandas==1.5.3
pickleshare==0.7.5
pillow==10.2.0
pip==23.3.1
ptyprocess==0.7.0
pymunk==6.7.0
pyparsing==3.0.9
pytest==7.4.0
PyYAML==6.0.1
SciencePlots==2.1.1
scikit-image==0.22.0
scipy==1.12.0
seaborn==0.12.2
setuptools==68.2.2
shapely==2.0.1
six==0.16.0
sknw==0.15
stack-data==0.2.0
tornado==6.3.3
tqdm==4.66.2
```

For the full dependency list, please refer to:

```text
requirements.txt
```

---

## 🚀 Usage

### ▶️ Quick Demo

Run the default 2D ship–ice navigation simulation.

Default settings:

- Channel size: **15 m × 80 m**
- Ice concentration: **20%–50%**
- Ship speed: **0.3 m/s**

```bash
python demo_sim2d_ship_ice_navigation.py
```

Specify ice density:

```bash
python demo_sim2d_ship_ice_navigation.py --ice_density 0.3
```

---

## 🧪 Batch Experiments

Run batch simulations with different planners and ice concentrations:

```bash
python -m ship_ice_planner.experiments.sim_exp \
    --run_name SAMPLE_RUN \
    --planners straight skeleton lattice \
    --method_names Straight Skeleton Proposed \
    --no_anim
```

This command runs simulations under ice concentrations from **20% to 50%**.

---

## 📈 Evaluation

Generate performance metrics and visualizations:

```bash
python evaluate_run_sim.py --run_name SAMPLE_RUN
```

Evaluation results are saved in the `output/` directory.

---

## 📁 Output

The generated results include:

- 🧭 Ship trajectory plots
- 💥 Collision records
- 📊 Performance metrics
  - Path length
  - Number of collisions
  - Energy loss
  - Tracking error

Output files are saved in:

```text
output/
```

Supported output formats include:

- CSV
- PNG
- PDF

---

## 🗂️ Project Structure

```text
IceNav/
├── demo_sim2d_ship_ice_navigation.py    # Main demo script
├── evaluate_run_sim.py                  # Results analysis and visualization
├── ship_ice_planner/                    # Core planning module
│   ├── perception/                      # Environment perception
│   ├── planning/                        # Path planning: lattice + A*
│   ├── collision/                       # Collision cost optimization
│   └── experiments/                     # Batch experiment scripts
├── data/                                # Ice field datasets
├── output/                              # Simulation results
├── requirements.txt                     # Python dependencies
└── README.md
```

---

## 📜 License

This project is intended for **academic and competition use only**.

Commercial use requires permission from the authors.

---

## 📚 Citation

If you use IceNav in your research or competition project, please consider citing this repository.

```bibtex
@misc{icenav2026,
  title  = {IceNav: Dynamic Path Planning for Complex Sea States},
  author = {Andy},
  year   = {2026},
  url    = {https://github.com/yourusername/IceNav}
}
```

---

## 📬 Contact

For questions, issues, or collaboration, please open an issue or contact the project authors.
