# Mathematical Foundations of NOETIKO Framework

## Abstract
This document provides the rigorous mathematical derivation of the field topologies and thermodynamic mechanisms utilized in the NOETIKO simulations. It bridges Maxwellian electrodynamics (Coulomb Gauge) with stochastic thermodynamics.

---

## 1. Electrodynamics of the Zero-B Field Manifold

### 1.1 Lagrangian Formulation
The interaction is derived from the canonical QED Lagrangian density under minimal coupling:
$$\mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + \bar{\psi}(i\gamma^\mu D_\mu - m)\psi$$
Where the covariant derivative $D_\mu = \partial_\mu + ieA_\mu$ introduces the vector potential $A_\mu$. In the NOETIKO topology, we enforce the **force-free constraint**:
$$\vec{B} = \nabla \times \vec{A} \approx 0 \quad \text{inside the torus core}$$

### 1.2 Gauge Transformation & Aharonov-Bohm Phase
Despite $\vec{B}=0$, the vector potential $\vec{A}$ is topologically non-trivial. The physical significance is revealed via the gauge-invariant phase factor (Berry Phase) accumulated by the biological wavefunction $\psi$:
$$\gamma_B = \frac{e}{\hbar} \oint_{\partial \Omega} \vec{A} \cdot d\vec{l}$$
This confirms that information is transferred via the phase $\Delta \phi$, not amplitude energy, solving the thermodynamic paradox.

---

## 2. Stochastic Resonance: The Kramers-Moyal Expansion

To bridge the activation energy gap $\kappa$, we model the probability density $P(x,t)$ using the Fokker-Planck equation derived from the Langevin dynamics:

### 2.1 The Langevin Driver
$$\frac{dx}{dt} = -\nabla V(x) + F_{signal}(t) + \sqrt{2D}\xi(t)$$
Where $F_{signal}(t) = A_0 \sin(\omega_H t)$ is the 1.42 GHz perturbation.

### 2.2 Escape Rate Derivation (Flux over Barrier)
Using the Kramers turnover rate, the escape time $T_{esc}$ becomes minimized at optimal noise $D_{opt}$:
$$R_{Kramers} \approx \frac{\omega_0 \omega_b}{2\pi \gamma} \exp\left(-\frac{\Delta V}{D}\right) \cosh\left(\frac{A_0 x_0}{D}\right)$$
The simulation validates that when $D \approx \kappa/2$, the coherent information transfer is maximized (SNR Peak).

---

## 3. Toroidal Manifold Topology (3D)

The bifilar winding is modeled as a loxodromic curve on the torus $T^2$:
$$\vec{r}(u,v) = \begin{pmatrix} (R+r\cos u)\cos v \\ (R+r\cos u)\sin v \\ r\sin u \end{pmatrix}$$
The winding path $\vec{\gamma}(t)$ satisfies the harmonic condition $u = Nv$ where $N=12$ (Winding Number), ensuring constructive interference of the A-field components while canceling the B-field flux.
