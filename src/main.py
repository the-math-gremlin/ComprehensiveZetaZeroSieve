import numpy as np
import os
from utils import load_parameters, load_data_files
from scipy.ndimage import gaussian_filter1d

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, t_values=None, limit=None, verbose=True):
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

    # Track correctly identified zeros
    true_positives = 0
    false_positives = 0
    missed_zeros = []
    detected_zeros = set()

    # Compare known zeros to the reconstructed envelope
    for zero in zeta_zeros:
        index = int(zero)  # Exact index, no rounding
        if index < len(envelope_reconstructed):
            delta_value = delta_curve[index]
            envelope_value = envelope_reconstructed[index]
            within_band = np.abs(delta_value - envelope_value) <= tolerance
            
            if within_band:
                true_positives += 1
                detected_zeros.add(zero)
            else:
                missed_zeros.append(zero)
                if verbose:
                    print(f"[DEBUG] Missed zero at t = {zero:.12f}, Delta = {delta_value:.6f}, Envelope = {envelope_value:.6f}")
        else:
            missed_zeros.append(zero)
            if verbose:
                print(f"[DEBUG] Zero {zero} is out of bounds for the envelope length.")

    # Identify false positives
    false_positives = []
    for idx in np.where(within_band_mask == 1)[0]:
        if idx not in detected_zeros:
            false_positives.append(idx)

    if verbose:
        print(f"True Positives: {true_positives}")
        print(f"False Positives: {len(false_positives)}")
        print(f"Missed Zeros: {len(missed_zeros)}")
        print(f"False Positive Indices: {false_positives[:10]}")  # Print first 10 false positives

    return true_positives, len(missed_zeros), len(false_positives), missed_zeros


if __name__ == "__main__":
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    t_values = np.arange(1, len(delta_curve) + 1, dtype=np.float64)
    run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, t_values=t_values, limit=None, verbose=True)
