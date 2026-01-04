# Project NOETIKO: 6-Dimensional Reality Engineering Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18020064.svg)](https://doi.org/10.5281/zenodo.18020064)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scientific Field](https://img.shields.io/badge/Field-Quantum_Biophysics-blue)](https://noetiko.org)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-validation%20complete-success)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18020064.svg)](https://doi.org/10.5281/zenodo.18020064)

## Overview
**Project NOETIKO** investigates the intersection of high-dimensional field theory and non-thermal biological regulation. This repository contains the *in-silico* validation scripts for the theoretical models published in our recent trilogy (Zenodo, 2025).

**Principal Investigator:** André Kappe (ORCID: [0009-0001-2799-379X](https://orcid.org/0009-0001-2799-379X))

## Key Concepts Validated
This repository provides numerical proofs for two core postulates of the NOETIKO framework:

1.  **Stochastic Resonance in Bio-Signaling:**
    Demonstrating how sub-threshold RF signals (1.42 GHz) utilize thermal noise ($k_B T$) to overcome the biological activation barrier ($\kappa \approx 1.0 \text{ eV}$). This resolves the thermodynamic paradox of weak-field interaction.

2.  **Vector Potential Topologies:**
    Simulating the magnetic vector potential ($\mathbf{A}$-field) distribution in a bifilar Möbius-Toroid configuration where the magnetic field $\mathbf{B} \approx 0$.

## Repository Structure
* `/simulations`: Python scripts for Stochastic Resonance and Field Topology.
* `/results`: Generated validation plots and visual data.
* `/docs`: References to the theoretical papers.

## Getting Started
You can run these simulations directly in your browser via Google Colab:
[Run in Google Colab](https://colab.research.google.com/) (Copy the script content into a new notebook).

## Citation
If you use this code or the theoretical framework, please cite the foundational trilogy:
> Kappe, A. (2025). *The NOETIKO Trilogy: Multidimensional Information Transfer in Biological Systems*. Zenodo. DOI: 10.5281/zenodo.18020064

## Simulation Constraints & Model Limitations
The current `noetiko_simulation_suite.py` utilizes specific approximations for computational efficiency:
* **A-Field Topology:** The Bifilar Möbius model uses a **2D cross-section approximation** of the vector potential ($\vec{A}$). The logarithmic potential formula (`-I * ln(r)`) assumes infinite wire length perpendicular to the plane, which is sufficient for demonstrating the *topology* of the zero-B-field zone but does not represent the full 3D toroidal curvature.
* **Signal Envelope:** The 1.42 GHz signal is modeled via its modulation envelope to visualize the *mechanism* of Stochastic Resonance without requiring nanosecond-resolution sampling of the carrier wave.

Future releases (v2.x) will implement full 3D Biot-Savart integration.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

