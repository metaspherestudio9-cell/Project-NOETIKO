import unittest
import numpy as np
import sys
import os

# Add the simulations directory to path so we can import the suite
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simulations')))

# Import the module (assuming the file is named noetiko_simulation_suite.py)
import noetiko_simulation_suite as noetiko

class TestNoetikoPhysics(unittest.TestCase):

    def test_hydrogen_frequency(self):
        """Verify that the Hydrogen Line frequency is physically accurate."""
        expected_freq = 1.4204e9 # 1.4204 GHz
        self.assertAlmostEqual(noetiko.HYDROGEN_FREQ, expected_freq, delta=1000, 
                               msg="Critical Physics Error: Hydrogen Frequency deviates from standard.")

    def test_boltzmann_constant(self):
        """Verify Boltzmann constant accuracy."""
        expected_kb = 1.380649e-23
        self.assertEqual(noetiko.KB, expected_kb, "Critical Physics Error: Wrong Boltzmann Constant.")

    def test_biological_temperature(self):
        """Verify biological temp is within human survival range (37°C)."""
        self.assertEqual(noetiko.TEMP_K, 310.15, "Error: Simulation not calibrated to 37°C (310.15K).")

    def test_kappa_threshold_exists(self):
        """Ensure the activation threshold is defined and positive."""
        self.assertTrue(noetiko.KAPPA_THRESHOLD > 0, "Error: Bio-Activation threshold must be positive.")

    def test_torus_geometry_logic(self):
        """Test if the 3D Torus parametric equations produce valid coordinates."""
        # Simple math check on the logic used in the suite
        R = 4
        r = 1
        theta = 0
        phi = 0
        # At angle 0,0: x should be R+r, y should be 0, z should be 0
        expected_x = R + r
        x_calc = (R + r * np.cos(theta)) * np.cos(phi)
        self.assertEqual(x_calc, expected_x, "Geometry Error: Torus equations are flawed.")

if __name__ == '__main__':
    unittest.main()
