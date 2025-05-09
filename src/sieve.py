import numpy as np

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None, verbose=False):
    amplitude = parameters["Amplitude"]
    frequency = parameters["Frequency"]
    sigma = parameters["Smoothing_Sigma"]
    tolerance = parameters["Tolerance"]

    true_positives = 0
    false_negatives = 0
    false_positives = 0

    # Set up logging if verbose mode is enabled
    if verbose:
        with open("sieve_diagnostics.log", "w") as log_file:
            log_file.write("Index, Within Band, Known Zero Match\n")

    for i in range(len(delta_curve)):
        # Apply limit if specified
        if limit is not None and i >= limit:
            break

        is_within_band = within_band_mask[i]
        known_zero_match = any(abs(i - zero) <= tolerance for zero in zeta_zeros)

        # Classify the index
        if is_within_band:
            if known_zero_match:
                true_positives += 1
            else:
                false_positives += 1
        else:
            if known_zero_match:
                false_negatives += 1

        # Log detailed diagnostics if enabled
        if verbose:
            with open("sieve_diagnostics.log", "a") as log_file:
                log_file.write(f"{i}, {is_within_band}, {known_zero_match}\n")

        # Optional progress indicator
        if verbose and i % 1000 == 0:
            print(f"[LOG] Checked index {i} / {limit if limit else len(delta_curve)}")

    return true_positives, false_negatives, false_positives
