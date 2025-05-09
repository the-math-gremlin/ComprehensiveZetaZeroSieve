import numpy as np
from utils import load_parameters, load_data_files
from sieve import run_sieve

def main(limit=None):
    # Load parameters and data files
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()

    # Print parameters for verification
    print(f"Final Parameters: {parameters}")

    # Run the sieve
    true_positives, false_negatives, false_positives = run_sieve(
        delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit
    )

    # Print results
    print(f"[INFO] True Positives: {true_positives}")
    print(f"[INFO] False Negatives: {false_negatives}")
    print(f"[INFO] False Positives: {false_positives}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the harmonic sieve for zeta zeros.")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of indices to check")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    main(limit=args.limit)
