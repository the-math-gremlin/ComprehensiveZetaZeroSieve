import argparse
import logging
from config import load_parameters
from sieve import run_sieve
from utils import load_data_files

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Comprehensive Zeta Zero Sieve")
    parser.add_argument("--mode", type=str, default="run", help="Mode to run the sieve (run, test, verify)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--limit", type=int, default=100000, help="Limit the number of indices to check")
    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="[%(levelname)s] %(message)s")

    # Load parameters
    params = load_parameters()
    logging.info(f"Final Parameters: {params}")

    # Load data files
    delta_curve, envelope, within_band_mask, known_zeros = load_data_files()
    logging.info(f"Delta Curve Length: {len(delta_curve)}")
    logging.info(f"Within Band Mask Length: {len(within_band_mask)}")
    logging.info(f"Number of Known Zeros: {len(known_zeros)}")

    # Run the sieve with the specified index limit
    true_positives, false_negatives, false_positives = run_sieve(delta_curve, envelope, within_band_mask, known_zeros, params, limit=args.limit)

    # Print the final counts
    logging.info(f"True Positives: {true_positives}")
    logging.info(f"False Negatives: {false_negatives}")
    logging.info(f"False Positives: {false_positives}")
    print(f"True Positives: {true_positives}")
    print(f"False Negatives: {false_negatives}")
    print(f"False Positives: {false_positives}")

if __name__ == "__main__":
    main()
