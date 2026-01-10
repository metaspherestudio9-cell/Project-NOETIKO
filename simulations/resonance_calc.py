#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NOETIKO RESONANCE ENGINE [CORE MODULE]
Version: 2.1 (Production)
Copyright (c) 2026 NOETIKO Research Division. All Rights Reserved.
Founder: André Kappe (ORCID: 0009-0001-2799-379X)

DESCRIPTION:
Calculates physical parameters for the Bifilar Möbius Emitter to achieve 
resonance with the Hydrogen Hyperfine Transition line (1.42 GHz).
"""

import math
import sys

class NoetikoResonator:
    def __init__(self):
        # PHYSICAL CONSTANTS
        self.c = 299792458  # Speed of Light (m/s)
        self.mu_0 = 4 * math.pi * 1e-7  # Vacuum permeability
        self.rho_copper = 1.68e-8  # Resistivity of Copper (Ohm*m)
        
        # TARGET PARAMETERS
        self.f_target = 1.420405751e9  # Hydrogen Line (Hz)

    def calculate_parameters(self):
        """Calculates precise wire lengths and skin depth with error handling."""
        try:
            if self.f_target <= 0:
                raise ValueError("Frequency must be positive.")
                
            lambda_0 = self.c / self.f_target
            omega = 2 * math.pi * self.f_target
            delta = math.sqrt((2 * self.rho_copper) / (omega * self.mu_0))
            
            return {
                "lambda_cm": lambda_0 * 100,
                "target_2lambda_cm": (lambda_0 * 2) * 100,
                "skin_depth_um": delta * 1e6
            }
        except Exception as e:
            print(f"Calculation Error: {e}")
            sys.exit(1)

    def run_audit(self):
        data = self.calculate_parameters()
        print("="*60)
        print("NOETIKO TECHNICAL AUDIT // 1.42 GHz RESONANCE")
        print("="*60)
        print(f"Target Frequency           : {self.f_target / 1e9:.9f} GHz")
        print(f"Fundamental Wavelength (λ) : {data['lambda_cm']:.6f} cm")
        print(f"Target Length (2λ - Halo)  : {data['target_2lambda_cm']:.6f} cm")
        print(f"Skin Depth (Gold Req.)     : {data['skin_depth_um']:.4f} µm")
        print("-" * 60)
        print("© 2026 NOETIKO Research Division. Cologne, NRW.")
        print("="*60)

if __name__ == "__main__":
    eng = NoetikoResonator()
    eng.run_audit()
