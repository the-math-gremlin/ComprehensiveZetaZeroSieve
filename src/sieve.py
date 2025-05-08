import numpy as np
from utils import log

def run_sieve(parameters, delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros):
    """
    Runs the core sieve algorithm to identify known zeta zeros within the allowed band.

    Parameters:
    - parameters (dict): Dictionary of sieve parameters.
    - delta_curve (np.ndarray): The precomputed delta curve.
    - dynamic_sine_envelope (np.ndarray): The dynamic sine envelope.
    - within_band_mask (np.ndarray): The binary mask indicating valid zero regions.
    - zeta_zeros (np.ndarray): The known nontrivial zeta zeros.

    Returns:
    - dict: Dictionary with true positives, false negatives, and false positives.
    """
    amplitude = parameters.get("Amplitude", 12.2)
    frequency = parameters.get("Frequency", 0.001)
    sigma = parameters.get("Smoothing_Sigma", 5.0)
    tolerance = parameters.get("Tolerance", 0.875)

    true_positives = []
    false_negatives = []
    false_positives = []

    # Validate alignment
    if delta_curve.shape != dynamic_sine_envelope.shape:
        raise ValueError("Delta curve and sine envelope are not aligned.")

    # Check each known zero
    known_zero_indices = set(np.round(zeta_zeros).astype(int))
    for zero in zeta_zeros:
        index = int(np.round(zero))
        if 0 <= index < len(within_band_mask) and within_band_mask[index]:
            true_positives.append(zero)
        else:
            false_negatives.append(zero)

    # Check for false positives with a tolerance
    tolerance_radius = int(np.ceil(tolerance * len(delta_curve) / len(zeta_zeros)))

    for i, is_within_band in enumerate(within_band_mask):
        if is_within_band and not any(abs(i - zero) <= tolerance_radius for zero in known_zero_indices):
            false_positives.append(i)
        
        # Add a progress logger for large files
        if i % 10000 == 0:
            log(f"Checked index {i} / {len(within_band_mask)}")


    # Log results
    log(f"True Positives: {len(true_positives)}")
    log(f"False Negatives: {len(false_negatives)}")
    log(f"False Positives: {len(false_positives)}")

    return {
        "True Positives": true_positives,
        "False Negatives": false_negatives,
        "False Positives": false_positives,
    }
