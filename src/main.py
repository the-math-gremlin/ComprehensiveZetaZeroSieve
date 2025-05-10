import numpy as np
import os
from utils import load_parameters, load_data_files
from scipy.ndimage import gaussian_filter1d
t_values = np.arange(1, len(delta_curve) + 1, dtype=np.float64)


def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, t_values=t_values, limit=None, verbose=True):
    # Load parameters
    amplitude = parameters["Amplitude"]
    base_frequency = parameters["Base_Frequency"]
    smoothing_sigma = parameters["Smoothing_Sigma"]
    tolerance = parameters["Tolerance"]

    # Calculate the smoothed centerline μ(t)
    mu_t = gaussian_filter1d(delta_curve, smoothing_sigma)

    # Phase shift
    phase_shift = parameters["Phase_Shift"]
    envelope_reconstructed = mu_t + amplitude * np.sin(
        (2 * np.pi * base_frequency * np.log(t_values + 1)) / np.log(3) + phase_shift
    )

    # Track correctly identified zeros
    true_positives = 0
    false_positives = 0
    missed_zeros = []

    # Compare known zeros to the reconstructed envelope
    for zero in zeta_zeros:
        index = int(np.floor(zero))
        if index < len(envelope_reconstructed):
            delta_value = delta_curve[index]
            envelope_value = envelope_reconstructed[index]
            within_band = np.abs(delta_value - envelope_value) <= tolerance
            
            if within_band:
                true_positives += 1
            else:
                missed_zeros.append(zero)
                if verbose:
                    print(f"[DEBUG] Missed zero at t = {zero:.12f}, Delta = {delta_value:.6f}, Envelope = {envelope_value:.6f}")
        else:
            missed_zeros.append(zero)
            if verbose:
                print(f"[DEBUG] Zero {zero} is out of bounds for the envelope length.")

    # Identify false positives
    false_positives = np.sum(within_band_mask) - true_positives

    if verbose:
        print(f"True Positives: {true_positives}")
        print(f"False Positives: {false_positives}")
        print(f"Missed Zeros: {len(missed_zeros)}")

    return true_positives, len(missed_zeros), false_positives, missed_zeros


if __name__ == "__main__":
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None, verbose=True)
