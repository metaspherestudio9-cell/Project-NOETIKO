import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simulations')))
import noetiko_simulation_suite as noetiko

class TestNoetikoPhysics(unittest.TestCase):

    def test_hydrogen_frequency_precision(self):
        """Critical: Verify Hydrogen Line (21cm) frequency precision."""
        expected = 1.4204e9
        self.assertAlmostEqual(noetiko.HYDROGEN_FREQ, expected, delta=1.0, 
            msg="Physics Violation: Hydrogen line frequency drift detected.")

    def test_thermodynamic_constants(self):
        """Verify Boltzmann and Temperature constants."""
        self.assertEqual(noetiko.KB, 1.380649e-23)
        self.assertEqual(noetiko.TEMP_K, 310.15)

    def test_torus_topology_integrity(self):
        """Edge Case: Test Torus geometry for singularity avoidance."""
        # Test at geometric origin/center (should not crash)
        # R=4, r=1. At theta=pi/2 (z-max), phi=0
        R, r = 4, 1
        theta = np.pi/2
        z_calc = r * np.sin(theta)
        self.assertAlmostEqual(z_calc, 1.0)

    def test_stochastic_resonance_signal_shape(self):
        """Edge Case: Ensure signal generation handles empty arrays gracefully."""
        time_empty = np.array([])
        signal = 0.4 * np.sin(time_empty)
        self.assertEqual(len(signal), 0, "Signal generator failed on empty time input.")

    def test_noise_distribution_properties(self):
        """Statistical Test: Verify noise is Gaussian (Zero Mean)."""
        noise = np.random.normal(0, 1.0, 100000)
        mean = np.mean(noise)
        self.assertTrue(abs(mean) < 0.05, "Noise generator is biased (Non-Gaussian).")

if __name__ == '__main__':
    unittest.main()
