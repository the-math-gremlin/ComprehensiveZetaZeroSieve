import numpy as np

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
    - true_positives (list): Zeros correctly identified within the band.
    - false_negatives (list): Zeros missed by the sieve.
    - false_positives (list): Points incorrectly identified as zeros.
    """
    amplitude = parameters["Amplitude"]
    frequency = parameters["Frequency"]
    sigma = parameters["Smoothing_Sigma"]
    tolerance = parameters["Tolerance"]

    true_positives = []
    false_negatives = []
    false_positives = []

    # Validate alignment
    if delta_curve.shape != dynamic_sine_envelope.shape:
        raise ValueError("Delta curve and sine envelope are not aligned.")

    # Check each known zero
    for zero in zeta_zeros:
        index = int(np.round(zero))  # Round to the nearest index
        if 0 <= index < len(within_band_mask) and within_band_mask[index]:
            true_positives.append(zero)
        else:
            false_negatives.append(zero)

    # Check for false positives
    known_zero_indices = set(np.round(zeta_zeros).astype(int))
    for i, is_within_band in enumerate(within_band_mask):
        if is_within_band and (i not in known_zero_indices):
            false_positives.append(i)

    return true_positives, false_negatives, false_positives
