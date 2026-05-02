# IceNav: Dynamic Path Planning for Complex Sea States
IceNav is a real-time local navigation system for autonomous vessels navigating through broken ice fields (20%–50% ice concentration) with ice drift speeds up to 0.5 m/s. It generates safe, smooth, and dynamically feasible paths while significantly reducing collision risk and kinetic energy loss.
# Key Features
Real-time Replanning: Receding horizon strategy + lattice planner with <90ms update cycle (7–10 Hz replanning frequency)
Collision Cost Optimization: Physics-based 2D inelastic collision model minimizing kinetic energy loss; prioritizes avoiding large ice blocks (>50 kg) and head-on collisions (>60°)
Ship Dynamics Constraints: Minimum turning radius 1.5 m, max angular velocity 0.5 rad/s, max acceleration 0.2 m/s²
Two-Stage Path Planning: Improved A* for initial path + optimization refinement for smoothness and safety
Simulation Framework: Integrated with Pymunk physics engine and Marine Systems Simulator (MSS)
# Performance Comparison
Compared to straight line method: Collisions ↓61.3%, Energy loss ↓59.1%, Position error ↓31.8%
# System Architecture
Perception Module → Path Planning → Collision Optimization → Simulation/Control
Collision Optimization → Real-time Feedback → Perception Module
Perception Module: Sensor fusion (camera, millimeter-wave radar, IMU or pre-generated ice field datasets); 10 Hz 2D environment model update
Path Planning: Lattice planner + improved A* with embedded dynamics constraints
Collision Optimization: Kinetic energy loss cost function with multi-objective weights (path length 0.4, collision cost 0.5, ice concentration penalty 0.1)
Simulation Module: Pymunk + MSS, supports trajectory visualization and performance evaluation
# Installation
# Requirements
Python 3.9
Linux (Ubuntu 20.04) 

# Dependencies
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
six==1.16.0
sknw==0.15
stack-data==0.2.0
tornado==6.3.3
tqdm==4.66.2
# Setup
# Clone repository
git clone https://github.com/yourusername/IceNav.git
cd IceNav

# Create Conda environment
conda create -n py39 python=3.9
conda activate py39

# Install dependencies
pip install -r requirements.txt

# Download ice field dataset (400 ice fields, ~500MB)
# Download from cloud storage link and extract to data/

# Usage
# Quick Demo
# Run default 2D simulation (channel 15m×80m, ice density 0.2-0.5, ship speed 0.3 m/s)
python demo_sim2d_ship_ice_navigation.py

# Specify ice density
python demo_sim2d_ship_ice_navigation.py --ice_density 0.3

# Batch Experiments
# Run 1200 simulations (ice concentration 20%–50%)
python -m ship_ice_planner.experiments.sim_exp \
    --run_name SAMPLE_RUN \
    --planners straight skeleton lattice \
    --method_names Straight Skeleton Proposed \
    --no_anim

# Generate performance metrics and visualizations
python evaluate_run_sim.py --run_name SAMPLE_RUN

# Output
Results are saved to output/ directory (CSV, PNG, PDF formats), including:
Ship trajectory plots
Collision records
Performance metrics (path length, collisions, energy loss, tracking error)

# Project Structure
IceNav/
├── demo_sim2d_ship_ice_navigation.py   # Main demo script
├── evaluate_run_sim.py                 # Results analysis & visualization
├── ship_ice_planner/                   # Core planning module
│   ├── perception/                     # Environment perception
│   ├── planning/                       # Path planning (lattice + A*)
│   ├── collision/                      # Collision cost optimization
│   └── experiments/                    # Batch experiment scripts
├── data/                               # Ice field datasets
├── output/                             # Simulation results
├── requirements.txt                    # Python dependencies
└── README.md

License
For academic and competition use only. Commercial use requires permission from the authors.
