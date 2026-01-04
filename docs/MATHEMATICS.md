# Mathematical Framework of NOETIKO

This document details the field equations and topological derivations used in the `noetiko_simulation_suite.py`.

## 1. Stochastic Resonance & Arrhenius Activation
The probability $P$ of a bio-information packet crossing the activation barrier $\kappa$ is modeled using a modified Kramer's Rate Law driven by the Hydrogen line frequency $f_H$.

### Activation Probability
$$P(t) = A \cdot \exp\left(-\frac{\kappa - [S(t) + \xi(t)]}{k_B T}\right)$$

Where:
* $\kappa \approx 1.0 \, \text{eV}$: The bio-informational activation barrier.
* $S(t) = A_0 \sin(2\pi f_H t)$: The carrier signal at $f_H = 1420.4 \, \text{MHz}$.
* $\xi(t)$: Gaussian white noise (thermal bath) with intensity $D$.
* $k_B T$: Thermal energy at 310.15 K.

The simulation validates that when $S(t) \ll \kappa$, the addition of optimal noise intensity $\xi_{opt}$ maximizes the signal-to-noise ratio (SNR) via Stochastic Resonance.

---

## 2. Vector Potential Topology (Bifilar Möbius)
In the Aharonov-Bohm regime, the magnetic field $\vec{B}$ is canceled, but the vector potential $\vec{A}$ remains non-zero and carries the topological phase information.

### 2D Approximation (Cross-Section)
For the gradient analysis, we approximate the counter-propagating currents $I$ and $-I$ as infinite filaments:

$$\vec{A}_{total} = \frac{\mu_0 I}{2\pi} \ln\left(\frac{r_-}{r_+}\right) \hat{z}$$

This generates the "HEIL-Zone" gradient visualized in Figure 2.

### 3D Toroidal Manifold
The full geometry visualized in Figure 3 is defined by the parametric equations of a torus with major radius $R$ and minor radius $r$:

$$x(\theta, \phi) = (R + r \cos \theta) \cos \phi$$
$$y(\theta, \phi) = (R + r \cos \theta) \sin \phi$$
$$z(\theta, \phi) = r \sin \theta$$

The Bifilar Winding follows the path $\gamma(t)$ on this manifold:
$$\gamma(t) = \begin{bmatrix} (R + (r+\delta)\cos(N t))\cos t \\ (R + (r+\delta)\cos(N t))\sin t \\ (r+\delta)\sin(N t) \end{bmatrix}$$

Where $N=12$ is the winding number (harmonic resonance).
