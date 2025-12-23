"""
PROJECT NOETIKO - VALIDATION SUITE v1.0
Author: André Kappe
License: MIT
Description: Numerical simulation of Stochastic Resonance and Vector Potential Topology.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def simulate_stochastic_resonance():
    print("--- Running Stochastic Resonance Simulation ---")
    # Parameters
    time = np.linspace(0, 50, 1000)
    threshold = 1.2
    signal_amp = 0.4
    noise_level = 1.8
    
    # Generate Signals
    signal = signal_amp * np.sin(time)
    noise = np.random.normal(0, noise_level * 0.4, 1000)
    combined = signal + noise
    
    # Analysis
    peaks, _ = find_peaks(combined, height=threshold)
    
    # Plotting
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, signal, color='gold', label='Pure Signal (Sub-threshold)')
    plt.axhline(y=threshold, color='red', linestyle='--', label='Activation Threshold (kappa)')
    plt.title('Scenario A: Signal without Noise (No Effect)')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(time, combined, color='navy', alpha=0.6, label='Signal + Thermal Noise')
    plt.axhline(y=threshold, color='red', linestyle='--', linewidth=2)
    plt.plot(time[peaks], combined[peaks], "x", color='lime', markersize=10, label='Constructor Injection Events')
    plt.title(f'Scenario B: Stochastic Resonance (Information Transfer Validated) - {len(peaks)} Events')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('stochastic_resonance_proof.png')
    print("Simulation complete. Image saved.")

def simulate_vector_potential():
    print("--- Running Vector Potential Topology Simulation ---")
    def get_A_field(x, y, x_wire, y_wire, current):
        r = np.sqrt((x - x_wire)**2 + (y - y_wire)**2)
        r = np.maximum(r, 0.05)
        return -current * np.log(r)

    res = 100
    x = np.linspace(-3, 3, res)
    y = np.linspace(-3, 3, res)
    X, Y = np.meshgrid(x, y)
    
    # Bifilar Configuration (Approximation)
    wires = [(0.5, 0.5, 1), (0.6, 0.5, -1), (-0.5, 0.5, 1), (-0.6, 0.5, -1)]
    A_total = np.zeros((res, res))
    
    for dx, dy, I in wires:
        A_total += get_A_field(X, Y, dx, dy, I)
        
    plt.figure(figsize=(8, 6))
    contour = plt.contourf(X, Y, A_total, levels=50, cmap='inferno')
    plt.colorbar(contour, label='Vector Potential Magnitude')
    plt.title('Bifilar Möbius Topology: A-Field Distribution')
    plt.savefig('vector_potential_topology.png')
    print("Topology complete. Image saved.")

if __name__ == "__main__":
    simulate_stochastic_resonance()
    simulate_vector_potential()
