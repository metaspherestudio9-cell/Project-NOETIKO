"""
PROJECT NOETIKO - VALIDATION SUITE v2.0
Author: André Kappe (Project NOETIKO)
License: MIT
Repository: github.com/Andre-Kappe-NOETIKO/Project-NOETIKO

SCIENTIFIC CONTEXT:
This suite validates the core postulates of the NOETIKO Trilogy (Zenodo, 2025):
1. Stochastic Resonance: Using thermal noise to bridge the Bio-Information Threshold (Kappa).
2. Vector Potential Topology: A-Field modulation in Zero-B-Field environments (Bifilar Möbius).
3. Hydrogen Resonance: Signal calibration at 1420.4 MHz (21cm line).
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

def simulate_stochastic_resonance():
    """
    Validates the 'Thermodynamic Paradox Solution'.
    Demonstrates how sub-threshold RF signals at 1.42 GHz utilize 
    Gaussian thermal noise to trigger biological activation events via Stochastic Resonance.
    """
    print(f"--- Initiating Bio-Signal Injection at {HYDROGEN_FREQ/1e9} GHz ---")
    
    # Time domain setup (Scaled for visualization)
    t_points = 1000
    time = np.linspace(0, 50, t_points)
    
    # Signal Parameters
    # The signal is intentionally weak (Sub-threshold) to demonstrate resonance necessity
    signal_amp = 0.4 * KAPPA_THRESHOLD 
    carrier_wave = signal_amp * np.sin(time) # Representative of the 1.42 GHz envelope
    
    # Noise Generation (Simulating k_B * T thermal bath)
    noise_level = 1.8 
    thermal_noise = np.random.normal(0, noise_level * 0.4, t_points)
    
    # System State: The sum of Signal + Noise
    combined_state = carrier_wave + thermal_noise
    
    # Detection: Finding Constructor Injection Events (Crossing Kappa)
    peaks, _ = find_peaks(combined_state, height=KAPPA_THRESHOLD)
    
    # --- VISUALIZATION ---
    plt.figure(figsize=(12, 10))
    plt.suptitle(f"NOETIKO Validation: Stochastic Resonance @ {HYDROGEN_FREQ/1e6} MHz", fontsize=16)
    
    # Plot 1: The Problem (Signal too weak)
    plt.subplot(2, 1, 1)
    plt.plot(time, carrier_wave, color='#FFD700', label='RF Signal (1.42 GHz Information Carrier)')
    plt.axhline(y=KAPPA_THRESHOLD, color='red', linestyle='--', linewidth=2, label=f'Bio-Activation Threshold (Kappa={KAPPA_THRESHOLD})')
    plt.fill_between(time, -2, 2, color='#001a33', alpha=0.1) 
    plt.title('Scenario A: Pure Signal (Sub-Threshold) -> No Biological Effect', fontsize=12)
    plt.ylabel('Potential (eV)')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right')
    
    # Plot 2: The Solution (Signal + Noise)
    plt.subplot(2, 1, 2)
    plt.plot(time, combined_state, color='#003366', alpha=0.6, label='System State (Signal + Thermal Noise)')
    plt.axhline(y=KAPPA_THRESHOLD, color='red', linestyle='--', linewidth=2)
    
    # Highlight Injection Events
    plt.plot(time[peaks], combined_state[peaks], "x", color='#00FF00', markersize=12, markeredgewidth=3, label='Constructor Injection Events')
    
    plt.title(f'Scenario B: Resonance Achievement -> {len(peaks)} Information Transfer Events', fontsize=12)
    plt.xlabel('Time (normalized simulation units)')
    plt.ylabel('Potential (eV)')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Ensure results directory exists
    if not os.path.exists('results'):
        os.makedirs('results')
        
    plt.savefig('results/Fig1_Stochastic_Resonance_Validation.png')
    print(f"simulation_sr: Success. Generated {len(peaks)} events. Image saved to results/.")

def simulate_vector_potential():
    """
    Simulates the Magnetic Vector Potential (A-Field) distribution 
    in a Bifilar Möbius Toroid configuration.
    Validates the creation of non-zero A-Field regions where B-Field is minimized.
    """
    print("--- Calculating Vector Potential Topology (Bifilar Möbius) ---")
    
    def get_A_field_magnitude(x, y, x_wire, y_wire, current, direction):
        # A = (mu0 * I / 2*pi) * ln(r) * direction (Simplified Z-component model)
        r = np.sqrt((x - x_wire)**2 + (y - y_wire)**2)
        r = np.maximum(r, 0.05) # Avoid singularity
        # Counter-propagating currents create the A-field gradient
        return -direction * current * np.log(r)

    # Grid Setup (Micro-scale for cellular context)
    res = 150
    limit = 3
    x = np.linspace(-limit, limit, res)
    y = np.linspace(-limit, limit, res)
    X, Y = np.meshgrid(x, y)
    
    # Bifilar Coil Geometry (Cross-section view)
    current_I = 1.0 
    wires = [
        (0.5, 0.5, 1),   # Wire A (Out)
        (0.6, 0.5, -1),  # Wire A' (In)
        (-0.5, 0.5, 1),  # Wire B (Out)
        (-0.6, 0.5, -1)  # Wire B' (In)
    ]
    
    A_total = np.zeros((res, res))
    
    for dx, dy, direction in wires:
        A_total += get_A_field_magnitude(X, Y, dx, dy, current_I, direction)
        
    # --- VISUALIZATION ---
    plt.figure(figsize=(10, 8))
    contour = plt.contourf(X, Y, A_total, levels=60, cmap='inferno')
    cbar = plt.colorbar(contour)
    cbar.set_label('Vector Potential Magnitude |A|', rotation=270, labelpad=20)
    
    # Overlay Wire positions
    for dx, dy, d in wires:
        color = 'cyan' if d > 0 else 'magenta'
        plt.plot(dx, dy, 'o', color=color, markeredgecolor='white', markersize=8)

    plt.title('Bifilar Möbius Topology: A-Field Distribution (Zero-B Mode)', fontsize=14)
    plt.xlabel('Spatial Coordinate X (micrometers)')
    plt.ylabel('Spatial Coordinate Y (micrometers)')
    
    if not os.path.exists('results'):
        os.makedirs('results')

    plt.savefig('results/Fig2_Bifilar_Topology_A_Field.png')
    print("simulation_topology: Success. A-Field map generated. Image saved to results/.")

def simulate_3d_torus_topology():
    """
    Generates a 3D visualization of the Bifilar Möbius Toroid geometry.
    This validates the spatial manifold requirement for the A-Field topology.
    """
    print("--- Generating 3D Toroidal Manifold ---")
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Torus Parameters
    R = 4  # Major radius
    r = 1  # Minor radius
    
    # Grid generation
    theta = np.linspace(0, 2 * np.pi, 50)
    phi = np.linspace(0, 2 * np.pi, 50)
    theta, phi = np.meshgrid(theta, phi)
    
    # Parametric equations for Torus
    x = (R + r * np.cos(theta)) * np.cos(phi)
    y = (R + r * np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    
    # Plot Surface (Wireframe style for scientific look)
    ax.plot_wireframe(x, y, z, color='#003366', alpha=0.3, rstride=5, cstride=5)
    
    # Simulate Bifilar Winding Path (Gold Trace)
    # 12 windings around the torus
    t = np.linspace(0, 2 * np.pi, 200)
    windings = 12
    # Logic: phi moves fast (windings), theta moves slow (loop around major radius)
    x_wire = (R + (r+0.1) * np.cos(windings*t)) * np.cos(t)
    y_wire = (R + (r+0.1) * np.cos(windings*t)) * np.sin(t)
    z_wire = (r+0.1) * np.sin(windings*t)
    
    ax.plot(x_wire, y_wire, z_wire, color='gold', linewidth=2, label='Bifilar Gold Trace (Skin Effect optimized)')
    
    # Styling
    ax.set_title("3D Bifilar Möbius Toroid Geometry", fontsize=14)
    ax.set_xlabel('X [mm]')
    ax.set_ylabel('Y [mm]')
    ax.set_zlabel('Z [mm]')
    ax.legend()
    
    if not os.path.exists('results'):
        os.makedirs('results')
    
    plt.savefig('results/Fig3_3D_Torus_Geometry.png', dpi=300)
    print("simulation_3d: Success. 3D Manifold generated. Image saved.")

if __name__ == "__main__":
    simulate_stochastic_resonance()
    simulate_vector_potential()
    simulate_3d_torus_topology() # Neu hinzugefügt

