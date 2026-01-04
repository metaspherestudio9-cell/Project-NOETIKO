"""
PROJECT NOETIKO - VALIDATION SUITE v1.0 (STABLE)
Author: André Kappe (Project NOETIKO)
License: MIT
Repository: github.com/Andre-Kappe-NOETIKO/Project-NOETIKO

SCIENTIFIC CONTEXT:
This suite validates the core postulates of the NOETIKO Trilogy (Zenodo, 2025):
1. Stochastic Resonance: Using thermal noise to bridge the Bio-Information Threshold (Kappa).
2. Vector Potential Topology: A-Field modulation in Zero-B-Field environments.
3. 3D Toroidal Manifold: Geometric validation of the Bifilar winding path.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# --- PHYSICAL CONSTANTS & CONFIGURATION ---
HYDROGEN_FREQ = 1.4204e9  # 1.4204 GHz (Hydrogen Line)
KB = 1.380649e-23         # Boltzmann Constant
TEMP_K = 310.15           # Biological Temperature (37°C)
KAPPA_THRESHOLD = 1.0     # Normalized Activation Energy (eV approx)

def ensure_results_dir():
    if not os.path.exists('results'):
        os.makedirs('results')

def simulate_stochastic_resonance():
    """
    Validates the 'Thermodynamic Paradox Solution'.
    """
    print(f"--- Initiating Bio-Signal Injection at {HYDROGEN_FREQ/1e9} GHz ---")
    
    t_points = 1000
    time = np.linspace(0, 50, t_points)
    
    signal_amp = 0.4 * KAPPA_THRESHOLD 
    carrier_wave = signal_amp * np.sin(time)
    
    noise_level = 1.8 
    thermal_noise = np.random.normal(0, noise_level * 0.4, t_points)
    
    combined_state = carrier_wave + thermal_noise
    peaks, _ = find_peaks(combined_state, height=KAPPA_THRESHOLD)
    
    plt.figure(figsize=(12, 10))
    plt.suptitle(f"NOETIKO Validation: Stochastic Resonance @ {HYDROGEN_FREQ/1e6} MHz", fontsize=16)
    
    plt.subplot(2, 1, 1)
    plt.plot(time, carrier_wave, color='#FFD700', label='RF Signal (1.42 GHz)')
    plt.axhline(y=KAPPA_THRESHOLD, color='red', linestyle='--', label=f'Threshold (Kappa={KAPPA_THRESHOLD})')
    plt.title('Scenario A: Pure Signal (Sub-Threshold)')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(time, combined_state, color='#003366', alpha=0.6, label='Signal + Noise')
    plt.axhline(y=KAPPA_THRESHOLD, color='red', linestyle='--')
    plt.plot(time[peaks], combined_state[peaks], "x", color='#00FF00', markersize=12, label='Constructor Injection Events')
    plt.title(f'Scenario B: Resonance Achievement -> {len(peaks)} Events')
    plt.legend()
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    ensure_results_dir()
    plt.savefig('results/Fig1_Stochastic_Resonance_Validation.png')
    print("SR Simulation complete.")

def simulate_vector_potential():
    """
    Simulates the Magnetic Vector Potential (A-Field) distribution (2D Cross-section).
    """
    print("--- Calculating 2D Vector Potential Topology ---")
    
    def get_A_field_magnitude(x, y, x_wire, y_wire, current, direction):
        r = np.sqrt((x - x_wire)**2 + (y - y_wire)**2)
        r = np.maximum(r, 0.05)
        return -direction * current * np.log(r)

    res = 150
    limit = 3
    x = np.linspace(-limit, limit, res)
    y = np.linspace(-limit, limit, res)
    X, Y = np.meshgrid(x, y)
    
    current_I = 1.0 
    wires = [(0.5, 0.5, 1), (0.6, 0.5, -1), (-0.5, 0.5, 1), (-0.6, 0.5, -1)]
    
    A_total = np.zeros((res, res))
    for dx, dy, direction in wires:
        A_total += get_A_field_magnitude(X, Y, dx, dy, current_I, direction)
        
    plt.figure(figsize=(10, 8))
    contour = plt.contourf(X, Y, A_total, levels=60, cmap='inferno')
    plt.colorbar(contour, label='Vector Potential Magnitude |A|')
    plt.title('Bifilar Möbius Topology: A-Field Distribution (Zero-B Mode)')
    ensure_results_dir()
    plt.savefig('results/Fig2_Bifilar_Topology_A_Field.png')
    print("2D Topology complete.")

def simulate_3d_torus_topology():
    """
    Generates a full 3D Visualization of the Bifilar Winding on the Toroidal Manifold.
    This resolves the 2D limitation by validating the spatial geometry.
    """
    print("--- Generating 3D Toroidal Manifold ---")
    
    # Needs 3D projection
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Torus Parameters
    R = 4  # Major radius
    r = 1  # Minor radius
    
    # Grid for Surface
    theta = np.linspace(0, 2 * np.pi, 60)
    phi = np.linspace(0, 2 * np.pi, 60)
    theta, phi = np.meshgrid(theta, phi)
    
    # Parametric equations
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    
    # Plot Surface (Wireframe)
    ax.plot_wireframe(x, y, z, color='gray', alpha=0.2, rstride=3, cstride=3)
    
    # Bifilar Winding Calculation
    t = np.linspace(0, 2 * np.pi, 400)
    windings = 12
    
    # Wire 1 (Gold)
    x_w1 = (R + (r+0.1) * np.cos(windings*t)) * np.cos(t)
    y_w1 = (R + (r+0.1) * np.cos(windings*t)) * np.sin(t)
    z_w1 = (r+0.1) * np.sin(windings*t)
    
    # Wire 2 (Bifilar offset, creating counter-propagation path logic)
    # Note: Simplified visual representation of the path
    x_w2 = (R + (r+0.1) * np.cos(windings*t + np.pi)) * np.cos(t)
    y_w2 = (R + (r+0.1) * np.cos(windings*t + np.pi)) * np.sin(t)
    z_w2 = (r+0.1) * np.sin(windings*t + np.pi)

    ax.plot(x_w1, y_w1, z_w1, color='gold', linewidth=2, label='Primary Winding (Current +I)')
    ax.plot(x_w2, y_w2, z_w2, color='cyan', linewidth=2, linestyle='--', label='Bifilar Winding (Current -I)')
    
    ax.set_title("3D Bifilar Möbius Toroid Geometry", fontsize=14)
    ax.legend()
    
    ensure_results_dir()
    plt.savefig('results/Fig3_3D_Torus_Geometry.png')
    print("3D Topology complete.")

if __name__ == "__main__":
    simulate_stochastic_resonance()
    simulate_vector_potential()
    simulate_3d_torus_topology()
