import numpy as np
import os

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None):
    """Run the harmonic sieve to identify true zeta zeros with detailed diagnostics."""
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

    # Create or clear the diagnostic log
    diagnostic_file = "sieve_diagnostics.log"
    if os.path.exists(diagnostic_file):
        os.remove(diagnostic_file)

    with open(diagnostic_file, "w") as log_file:
        log_file.write("[DIAGNOSTIC LOG] Sieve Run Analysis\n")
        log_file.write("=" * 40 + "\n\n")

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
                    log_file.write(f"[False Positive] Index: {i}, Delta: {delta_curve[i]}, Envelope: {envelope_reconstructed[i]}\n")
            elif is_near_known_zero:
                false_negatives += 1
                log_file.write(f"[Missed Zero] Index: {i}, Delta: {delta_curve[i]}, Envelope: {envelope_reconstructed[i]}\n")

        # Final results
        log_file.write("\n[INFO] Sieve run completed.\n")
        log_file.write(f"[INFO] True Positives: {true_positives}\n")
        log_file.write(f"[INFO] False Negatives: {false_negatives}\n")
        log_file.write(f"[INFO] False Positives: {false_positives}\n")

    # Console output for summary
    print("\n[INFO] Sieve run completed.")
    print(f"[INFO] True Positives: {true_positives}")
    print(f"[INFO] False Negatives: {false_negatives}")
    print(f"[INFO] False Positives: {false_positives}")

    return true_positives, false_negatives, false_positives
