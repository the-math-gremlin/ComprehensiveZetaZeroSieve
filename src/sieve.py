import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Load known zeta zeros
zeta_zeros = np.load('zeta_zeros.npy')

# Sieve parameters from Deep Research
sigma = 5.0  # Smoothing width for mu(t)
A = 12.2  # Envelope amplitude (degrees)
f = 0.001  # Envelope frequency
phi = -0.0085  # Envelope phase shift
epsilon = 0.875  # Envelope tolerance (degrees)

# Define the raw modular drift function (Δ(t))
def raw_drift(t_values):
    ln3 = np.log(3)
    lnpi = np.log(np.pi)
    theta_3 = (2 * np.pi * np.log(t_values) / ln3) % (2 * np.pi)
    theta_pi = (2 * np.pi * np.log(t_values) / lnpi) % (2 * np.pi)
    drift = np.minimum(np.abs(theta_3 - theta_pi), 2 * np.pi - np.abs(theta_3 - theta_pi))
    drift_degrees = (drift / (2 * np.pi)) * 360
    return drift_degrees

# Generate the raw drift
delta_t = raw_drift(zeta_zeros)

# Smooth the drift to obtain mu(t)
mu_t = gaussian_filter1d(delta_t, sigma=sigma)

# Generate the harmonic envelope
envelope_t = mu_t + A * np.sin(f * np.log(zeta_zeros + 1) + phi)

# Apply the final capture condition
within_band_mask = np.abs(delta_t - envelope_t) <= epsilon
captured_zeros = zeta_zeros[within_band_mask]

# Print final results
captured_count = len(captured_zeros)
first_10_captured = np.round(captured_zeros[:10], 8)
last_10_captured = np.round(captured_zeros[-10:], 8)

print(f"Total Captured Zeros: {captured_count}")
print(f"First 10 Captured Zeros: {first_10_captured}")
print(f"Last 10 Captured Zeros: {last_10_captured}")

# Plot the drift, smoothed centerline, and envelope for verification
plt.figure(figsize=(14, 8))
plt.plot(zeta_zeros, delta_t, label="Δ(t) (Raw Drift)", color="blue", alpha=0.7)
plt.plot(zeta_zeros, mu_t, label="μ(t) (Smoothed Centerline)", color="green", alpha=0.6, linestyle='--')
plt.plot(zeta_zeros, envelope_t, label="E(t) (Harmonic Envelope)", color="orange", alpha=0.7)
plt.scatter(captured_zeros, delta_t[within_band_mask], color="red", s=10, label="Captured Zeros")
plt.title("Final Drift and Envelope Alignment")
plt.xlabel("t (Imaginary Part of Zero)")
plt.ylabel("Modular Drift (degrees)")
plt.legend()
plt.show()
