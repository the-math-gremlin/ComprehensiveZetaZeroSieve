import numpy as np

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None):
    """Run the harmonic sieve to identify true zeta zeros."""
    tolerance_radius = parameters["Tolerance"]
    phase_shift = parameters["Phase_Shift"]
    base_frequency = parameters["Base_Frequency"]
    seed_region_end = parameters["Seed_Region_End"]

    true_positives = 0
    false_negatives = 0
    false_positives = 0

    known_zero_indices = set(np.round(zeta_zeros).astype(int))

    for i in range(len(delta_curve) if limit is None else min(len(delta_curve), limit)):
        # Check if the point is within the allowed band
        is_within_band = within_band_mask[i]

        # Check for known zero proximity
        is_near_known_zero = any(abs(i - zero) <= tolerance_radius for zero in known_zero_indices)

        # Classify as a true positive, false positive, or false negative
        if is_within_band:
            if is_near_known_zero:
                true_positives += 1
            else:
                false_positives += 1
        elif is_near_known_zero:
            false_negatives += 1

    return true_positives, false_negatives, false_positives
