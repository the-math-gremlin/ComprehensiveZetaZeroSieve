import argparse
import logging
import numpy as np
from config import PARAMETERS_FILE, DELTA_CURVE_FILE, DYNAMIC_SINE_ENVELOPE_FILE, WITHIN_BAND_MASK_FILE, ZETA_ZEROS_FILE
from utils import load_parameters, save_results, log
from sieve import run_sieve

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
    params = load_parameters(PARAMETERS_FILE)
    logging.info(f"Final Parameters: {params}")

    # Load data files
    delta_curve = np.load(DELTA_CURVE_FILE)
    envelope = np.load(DYNAMIC_SINE_ENVELOPE_FILE)
    within_band_mask = np.load(WITHIN_BAND_MASK_FILE)
    known_zeros = np.load(ZETA_ZEROS_FILE)

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
