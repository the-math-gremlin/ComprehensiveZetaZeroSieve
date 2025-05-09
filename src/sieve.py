def run_sieve(delta_curve, envelope, within_band_mask, known_zeros, params, limit=100000):
    amplitude = params["Amplitude"]
    frequency = params["Frequency"]
    sigma = params["Smoothing_Sigma"]
    tolerance_radius = params["Tolerance"]

    # Convert known zeros to indices for faster lookup
    known_zero_indices = set(int(zero) for zero in known_zeros)

    true_positives = 0
    false_negatives = 0
    false_positives = 0

    for i, is_within_band in enumerate(within_band_mask[:limit]):
        if is_within_band:
            # Check if this index is a known zero
            if i in known_zero_indices:
                true_positives += 1
            else:
                false_positives += 1

        # Optional verbose logging for progress
        if i > 0 and i % 10000 == 0:
            print(f"[LOG] Checked index {i} / {limit}")

    false_negatives = len(known_zero_indices - set(range(limit)))

    return true_positives, false_negatives, false_positives
