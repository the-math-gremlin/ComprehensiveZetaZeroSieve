import numpy as np

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None):
    """Run the harmonic sieve to identify true zeta zeros."""
    A = parameters["Amplitude"]
    f = parameters["Base_Frequency"]
    sigma = parameters["Smoothing_Sigma"]
    tolerance_radius = int(np.ceil(parameters["Tolerance"] * 10))
    phase_shift = parameters["Phase_Shift"]
    seed_region_end = parameters["Seed_Region_End"]

    true_positives = 0
    false_negatives = 0
    false_positives = 0

    # Convert known zeros to indices
    known_zero_indices = set(np.round(zeta_zeros).astype(int))

    # Prepare the envelope for comparison
    t_values = np.arange(1, len(delta_curve) + 1)
    mu_t = np.convolve(delta_curve, np.ones(int(sigma)) / sigma, mode='same')
    envelope_reconstructed = mu_t + A * np.sin(2 * np.pi * f * np.log(t_values + 1) + phase_shift)

    for i in range(len(delta_curve) if limit is None else min(len(delta_curve), limit)):
        # Skip the seed region
        if i <= seed_region_end:
            continue

        # Check if this point is within the envelope band
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
