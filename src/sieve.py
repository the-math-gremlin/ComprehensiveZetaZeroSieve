import numpy as np

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, amplitude, frequency, sigma, tolerance):
    # Core sieve logic, comparing known zeros to calculated bands
    true_positives = []
    false_negatives = []
    false_positives = []

    # Basic envelope validation
    envelope_mismatch = np.any(dynamic_sine_envelope != delta_curve * amplitude)
    if envelope_mismatch:
        raise ValueError("Envelope and delta curve are not aligned.")

    # Check for known zeros within the allowed band
    for zero in zeta_zeros:
        index = int(zero)  # Assuming the zeros are indexed directly
        if within_band_mask[index]:
            true_positives.append(zero)
        else:
            false_negatives.append(zero)

    # Identify any false positives
    for i, in_band in enumerate(within_band_mask):
        if in_band and i not in zeta_zeros:
            false_positives.append(i)

    return true_positives, false_negatives, false_positives
