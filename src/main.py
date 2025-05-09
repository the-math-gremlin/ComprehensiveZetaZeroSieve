import argparse
from config import DEFAULT_PARAMETERS
from utils import load_parameters, load_data_files
from sieve import run_sieve

def main():
    parser = argparse.ArgumentParser(description="Comprehensive Zeta Zero Sieve")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of indices to process")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    # Load parameters and data files
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()

    # Print the loaded parameters for verification
    print("\nFinal Parameters:", parameters)

    # Run the sieve with the specified limit
    true_positives, false_negatives, false_positives = run_sieve(
        delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=args.limit, verbose=args.verbose
    )

    # Print summary
    print(f"True Positives: {true_positives}")
    print(f"False Negatives: {false_negatives}")
    print(f"False Positives: {false_positives}")

if __name__ == "__main__":
    main()
