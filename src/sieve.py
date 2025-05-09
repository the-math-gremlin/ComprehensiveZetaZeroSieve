import numpy as np

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None, verbose=False):
    tolerance_radius = parameters["Tolerance"]
    seed_region_end = parameters["Seed_Region_End"]

    # Convert known zero values to indices
    known_zero_indices = np.array([int(zero) for zero in zeta_zeros if zero < len(delta_curve)])

    true_positives = 0
    false_negatives = 0
    false_positives = 0

    # Initialize detected zero set
    detected_zero_indices = set()

    for i in range(len(delta_curve) if limit is None else limit):
        is_within_band = within_band_mask[i]
        if is_within_band and not any(abs(i - zero) <= tolerance_radius for zero in known_zero_indices):
            false_positives += 1
        elif is_within_band:
            true_positives += 1
            detected_zero_indices.add(i)

    # Calculate false negatives
    false_negatives = len(known_zero_indices) - true_positives

    if verbose:
        print(f"[INFO] True Positives: {true_positives}")
        print(f"[INFO] False Negatives: {false_negatives}")
        print(f"[INFO] False Positives: {false_positives}")

    return true_positives, false_negatives, false_positives
