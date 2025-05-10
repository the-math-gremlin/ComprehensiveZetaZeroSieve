import numpy as np
import os
from utils import load_parameters, load_data_files
from scipy.ndimage import gaussian_filter1d

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, parameters, t_values=None, limit=None, verbose=True):
    # Load parameters
    amplitude = parameters["Amplitude"]
    base_frequency = parameters["Base_Frequency"]
    smoothing_sigma = parameters["Smoothing_Sigma"]
    tolerance = parameters["Tolerance"]
    phase_shift = parameters["Phase_Shift"]

    # Calculate the smoothed centerline μ(t)
    mu_t = gaussian_filter1d(delta_curve, smoothing_sigma)

    # Use exact float64 for t_values
    if t_values is None:
        t_values = np.arange(1, len(delta_curve) + 1, dtype=np.float64)

    log_t_values = np.log(t_values + 1).astype(np.float64)
    envelope_reconstructed = mu_t + amplitude * np.sin(
        (2 * np.pi * base_frequency * log_t_values) / np.log(3) + phase_shift
    )

    # Track identified zeros
    detected_zeros = []

    # Sieve logic - independent of known zeros
    for idx, (delta_value, envelope_value) in enumerate(zip(delta_curve, envelope_reconstructed)):
        within_band = np.abs(delta_value - envelope_value) <= tolerance
        if within_band:
            detected_zeros.append(idx)

    # Print summary
    if verbose:
        print(f"Identified {len(detected_zeros)} potential zeros.")
        print(f"First 20 detected zeros: {detected_zeros[:20]}")

    return detected_zeros


if __name__ == "__main__":
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, _ = load_data_files()
    t_values = np.arange(1, len(delta_curve) + 1, dtype=np.float64)
    detected_zeros = run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, parameters, t_values=t_values, limit=None, verbose=True)
