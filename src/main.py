import numpy as np
import os
from utils import load_parameters, load_data_files
from scipy.ndimage import gaussian_filter1d

def run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None, verbose=False):
    A = parameters["Amplitude"]
    f = parameters["Base_Frequency"]
    sigma = parameters["Smoothing_Sigma"]
    tolerance_radius = int(np.ceil(parameters["Tolerance"] * 10))
    seed_region_end = parameters["Seed_Region_End"]

    true_positives = 0
    false_negatives = 0
    false_positives = 0
    missed_zeros = []
    known_zero_indices = set(zeta_zeros)

    # Prepare the envelope for comparison
    t_values = np.arange(1, len(delta_curve) + 1)
    mu_t = gaussian_filter1d(delta_curve, sigma)
    envelope_reconstructed = mu_t + A * np.sin(2 * np.pi * f * np.log(t_values + 1))

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
                missed_zeros.append(i)
                log_file.write(f"[Missed Zero] Index: {i}, Delta: {delta_curve[i]}, Envelope: {envelope_reconstructed[i]}\n")

            # Progress indicator
            if i % 10000 == 0 and i > seed_region_end:
                print(f"[INFO] Processed {i} indices...")

        # Log final results
        log_file.write("\n[INFO] Sieve run completed.\n")
        log_file.write(f"[INFO] True Positives: {true_positives}\n")
        log_file.write(f"[INFO] False Negatives: {false_negatives}\n")
        log_file.write(f"[INFO] False Positives: {false_positives}\n")
        log_file.write(f"[INFO] Known Missed Zeros: {missed_zeros}\n")

    # Console output for summary
    print("\n[INFO] Sieve run completed.")
    print(f"[INFO] True Positives: {true_positives}")
    print(f"[INFO] False Negatives: {false_negatives}")
    print(f"[INFO] False Positives: {false_positives}")
    print(f"[INFO] Known Missed Zeros: {missed_zeros}")

    return true_positives, false_negatives, false_positives, missed_zeros


def main(limit=None, verbose=False):
    # Load parameters and data files
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()

    # Print parameters for verification
    print(f"Final Parameters: {parameters}")

    # Run the sieve with diagnostics enabled
    true_positives, false_negatives, false_positives, missed_zeros = run_sieve(
        delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit, verbose
    )

    # Print final summary
    print(f"[INFO] True Positives: {true_positives}")
    print(f"[INFO] False Negatives: {false_negatives}")
    print(f"[INFO] False Positives: {false_positives}")
    print(f"[INFO] Known Missed Zeros: {missed_zeros}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the harmonic sieve for zeta zeros.")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of indices to check")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output with detailed diagnostics")
    args = parser.parse_args()

    main(limit=args.limit, verbose=args.verbose)
