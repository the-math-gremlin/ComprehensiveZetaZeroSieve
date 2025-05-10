import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Load known zeta zeros
zeta_zeros = np.load('../data/zeta_zeros.npy')

# Final, optimized sieve parameters
sigma_final = 3.6  # Optimized smoothing width
A_final = 12.445  # Final amplitude
phi_final = -0.00755  # Final phase correction
f_final = 0.001018  # Final frequency
epsilon = 0.875  # Envelope tolerance

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

# Apply the final optimized Gaussian smoothing
mu_t_final = gaussian_filter1d(delta_t, sigma=sigma_final)

# Generate the final harmonic envelope
envelope_t_final = mu_t_final + A_final * np.sin(f_final * np.log(zeta_zeros + 1) + phi_final)

# Apply the final capture condition
within_band_mask_final = np.abs(delta_t - envelope_t_final) <= epsilon
captured_zeros_final = zeta_zeros[within_band_mask_final]

# Verify the final missed zeros
missed_zeros_final = np.setdiff1d(zeta_zeros, captured_zeros_final)
missed_zero_count_final = len(missed_zeros_final)

# Print the final capture results
print(f"Total Captured Zeros: {len(captured_zeros_final)}")
print(f"Total Missed Zeros: {missed_zero_count_final}")
print(f"First 5 Missed Zeros: {missed_zeros_final[:5]}")

# Plot the final alignment for verification
plt.figure(figsize=(14, 8))
plt.plot(zeta_zeros, delta_t, label="Δ(t) (Raw Drift)", color="blue", alpha=0.7)
plt.plot(zeta_zeros, mu_t_final, label="μ(t) (Smoothed Centerline)", color="green", alpha=0.6, linestyle='--')
plt.plot(zeta_zeros, envelope_t_final, label="E(t) (Final Verified Envelope)", color="orange", alpha=0.7)
plt.title("Final Verified Drift and Envelope Alignment (Full Zero Range)")
plt.xlabel("t (Imaginary Part of Zero)")
plt.ylabel("Modular Drift (degrees)")
plt.legend()
plt.show()
