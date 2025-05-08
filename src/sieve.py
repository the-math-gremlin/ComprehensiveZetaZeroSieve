import numpy as np

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, amplitude, frequency, sigma, tolerance):
    """
    Runs the core sieve algorithm to identify known zeta zeros within the allowed band.

    Parameters:
    - delta_curve (np.ndarray): The precomputed delta curve.
    - dynamic_sine_envelope (np.ndarray): The dynamic sine envelope.
    - within_band_mask (np.ndarray): The binary mask indicating valid zero regions.
    - zeta_zeros (np.ndarray): The known nontrivial zeta zeros.
    - amplitude (float): Sine envelope amplitude.
    - frequency (float): Sine envelope frequency.
    - sigma (float): Smoothing parameter.
    - tolerance (float): Allowed deviation for zero detection.

    Returns:
    - true_positives (list): Zeros correctly identified within the band.
    - false_negatives (list): Zeros missed by the sieve.
    - false_positives (list): Points incorrectly identified as zeros.
    """
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

    # Identify false positives
    for i, in_band in enumerate(within_band_mask):
        if in_band and (i not in zeta_zeros):
            false_positives.append(i)

    return true_positives, false_negatives, false_positives


def verify_alignment(delta_curve, dynamic_sine_envelope):
    """
    Verifies that the delta curve and sine envelope are correctly aligned.

    Parameters:
    - delta_curve (np.ndarray): The precomputed delta curve.
    - dynamic_sine_envelope (np.ndarray): The dynamic sine envelope.

    Returns:
    - bool: True if aligned, False otherwise.
    """
    return delta_curve.shape == dynamic_sine_envelope.shape


def calculate_accuracy(true_positives, false_negatives, false_positives):
    """
    Calculates the accuracy metrics for the sieve.

    Parameters:
    - true_positives (list): Correctly identified zeros.
    - false_negatives (list): Missed zeros.
    - false_positives (list): Incorrectly identified zeros.

    Returns:
    - dict: Accuracy metrics.
    """
    total_zeros = len(true_positives) + len(false_negatives)
    accuracy = len(true_positives) / total_zeros if total_zeros > 0 else 0.0
    false_positive_rate = len(false_positives) / total_zeros if total_zeros > 0 else 0.0

    return {
        "accuracy": accuracy,
        "false_positive_rate": false_positive_rate,
        "true_positives": len(true_positives),
        "false_negatives": len(false_negatives),
        "false_positives": len(false_positives),
    }
