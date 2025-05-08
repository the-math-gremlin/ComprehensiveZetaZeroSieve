import numpy as np
from config import PARAMETERS_FILE, DELTA_CURVE_FILE, DYNAMIC_SINE_ENVELOPE_FILE, WITHIN_BAND_MASK_FILE, ZETA_ZEROS_FILE
from utils import load_parameters, save_results, log
from sieve import run_sieve
from verify_data import verify_data
import argparse

def main():
    # Verify the data files before running the sieve
    if not verify_data():
        print("[ERROR] Data verification failed. Please fix the data files and try again.")
        return

    # Load parameters
    params = load_parameters(PARAMETERS_FILE)

    # Load data files
    delta_curve = np.load(DELTA_CURVE_FILE)
    dynamic_sine_envelope = np.load(DYNAMIC_SINE_ENVELOPE_FILE)
    within_band_mask = np.load(WITHIN_BAND_MASK_FILE)
    zeta_zeros = np.load(ZETA_ZEROS_FILE)

    # Run the sieve
    try:
        results = run_sieve(params, delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros)
        
        # Print results if verbose mode is enabled
        if args.verbose:
            for key, value in results.items():
                print(f"{key}: {len(value)}")

        # Save results
        save_results("sieve_results.txt", results)
        log("[INFO] Sieve run completed successfully.")

    except Exception as e:
        print(f"[ERROR] Sieve run failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comprehensive Zeta Zero Sieve")
    parser.add_argument("--mode", choices=["run", "test"], default="run", help="Mode to run the sieve in")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    main()
