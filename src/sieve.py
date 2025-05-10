import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
from matplotlib.widgets import Slider

# Load the known zeta zeros
zeta_zeros = np.load('zeta_zeros.npy')

# Sieve parameters
sigma = 0.5
epsilon = 0.875
A_global = 12.20
phase_shift_global = -0.0100
f_global = 0.001018

# Define the globally consistent raw drift function
def simple_global_raw_drift(t_values):
    ln3 = np.log(3)
    lnpi = np.log(np.pi)
    # Corrected modular difference without special baseline adjustments
    drift = (2 * np.pi * (np.log(t_values) / ln3 - np.log(t_values) / lnpi)) % (2 * np.pi)
    # Apply a conservative global baseline correction
    baseline_correction = np.mean(drift) * 0.9  # Reduce correction strength to avoid early suppression
    drift -= baseline_correction  # Apply baseline correction
    # Ensure the drift is correctly scaled to 0-360 degrees
    drift_degrees = (drift / (2 * np.pi)) * 360
    drift_degrees = np.mod(drift_degrees, 360)
    return drift_degrees

# Generate the global raw drift
delta_t_global = simple_global_raw_drift(zeta_zeros)

# Apply Gaussian smoothing for the envelope centerline
gauss_kernel_final = np.ones(5) / 5  # Simple moving average as a final smoothing
mu_t_global = np.convolve(delta_t_global, gauss_kernel_final, mode='same')

# Generate the harmonic envelope
envelope_t_global = mu_t_global + A_global * np.sin(f_global * np.log(zeta_zeros + 1) + phase_shift_global)

# Apply the final capture condition
within_band_mask_global = np.abs(delta_t_global - envelope_t_global) <= epsilon
captured_zeros_global = zeta_zeros[within_band_mask_global]

# Print final results
captured_count_global = len(captured_zeros_global)
first_10_captured_global = np.round(captured_zeros_global[:10], 8)
last_10_captured_global = np.round(captured_zeros_global[-10:], 8)

print(f"Total Captured Zeros: {captured_count_global}")
print(f"First 10 Captured Zeros: {first_10_captured_global}")
print(f"Last 10 Captured Zeros: {last_10_captured_global}")

# Optional: plot the final alignment for verification
plt.figure(figsize=(14, 8))
plt.plot(zeta_zeros, delta_t_global, label="Δ(t) (Global Drift)", color="blue", alpha=0.7)
plt.plot(zeta_zeros, mu_t_global, label="μ(t) (Smoothed Drift)", color="green", alpha=0.6, linestyle='--')
plt.plot(zeta_zeros, envelope_t_global, label="E(t) (Harmonic Envelope)", color="orange", alpha=0.7)
plt.title("Global Drift and Envelope Alignment")
plt.xlabel("t (Imaginary Part of Zero)")
plt.ylabel("Modular Drift (degrees)")
plt.legend()
plt.show()
