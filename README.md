# Project NOETIKO: Bio-Physical Simulation Framework

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Release](https://img.shields.io/badge/Release-v1.0.0-blue)
![Science](https://img.shields.io/badge/Focus-Bio--Physics-green)

**Official Validation Repository for the NOETIKO Trilogy (Zenodo, 2025).**

## 1. Project Overview
Project NOETIKO investigates the intersection of **High-Dimensional Field Theory** and **Biological Regulation**. This repository contains the numerical simulation suite used to validate the core postulates of the NOETIKO framework:

1.  **Stochastic Resonance at 1.42 GHz:** Utilizing thermal noise ($k_B T$) to bridge the biological activation energy threshold ($\kappa \approx 1.0 \, \text{eV}$).
2.  **Vector Potential Topology:** Modeling the magnetic vector potential ($\vec{A}$) in bifilar Möbius-Toroid geometries where the magnetic field is canceled ($\vec{B} \approx 0$).

---

## 2. Key Scientific Concepts

### The Thermodynamic Solution
Biological systems operate in a thermal noise bath. Standard RF signals often fail to trigger bio-effects because they are below the activation threshold.
NOETIKO utilizes **Stochastic Resonance**, where the hydrogen line frequency ($f_H = 1420.4 \, \text{MHz}$) is phase-locked with thermal noise to push information packets over the $\kappa$-barrier.

### The Topological Interface
Information transfer is modeled not through amplitude modulation, but through topological phase shifts (Aharonov-Bohm effect) in the vector potential field, created by a specific **Bifilar Möbius Coil** design.

---

## 3. Validation Results

The following visualizations are generated directly by the `noetiko_simulation_suite.py` contained in this repository.

### Figure 1: Stochastic Resonance Validation
*Demonstrating the "Constructor Injection" mechanism where thermal noise amplifies the 1.42 GHz signal.*
![Stochastic Resonance](./results/Fig1_Stochastic_Resonance_Validation.png)

### Figure 2: Vector Potential Topology (2D Analysis)
*Heatmap of the $\vec{A}$-field distribution in the zero-magnetic-field zone of the bifilar coil.*
![Vector Potential](./results/Fig2_Bifilar_Topology_A_Field.png)

### Figure 3: 3D Toroidal Manifold
*Visualization of the Bifilar Winding Geometry on the Toroidal Manifold, validating the spatial requirements for the A-Field topology.*
![3D Torus](./results/Fig3_3D_Torus_Geometry.png)

---

## 4. Getting Started

### Prerequisites
* Python 3.8+
* Libraries: `numpy`, `matplotlib`, `scipy`

### Installation & Execution
You can reproduce these results locally or via Google Colab.

```bash
# Clone the repository
git clone [https://github.com/Andre-Kappe-NOETIKO/Project-NOETIKO.git](https://github.com/Andre-Kappe-NOETIKO/Project-NOETIKO.git)

# Navigate to the directory
cd Project-NOETIKO

# Install dependencies
pip install -r requirements.txt

# Run the simulation suite
python simulations/noetiko_simulation_suite.py

