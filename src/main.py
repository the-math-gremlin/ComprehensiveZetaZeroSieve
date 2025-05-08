import os
import numpy as np
import argparse
from sieve import run_sieve
from utils import load_parameters

# Set the paths to the data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
PARAMETERS_FILE = os.path.join(DATA_DIR, "sieve_parameters.txt")
DELTA_CURVE_FILE = os.path.join(DATA_DIR, "delta_curve.npy")
DYNAMIC_SINE_ENVELOPE_FILE = os.path.join(DATA_DIR, "dynamic_sine_envelope.npy")
WITHIN_BAND_MASK_FILE = os.path.join(DATA_DIR, "within_band_mask.npy")
ZETA_ZEROS_FILE = os.path.join(DATA_DIR, "zeta_zeros.npy")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Comprehensive Zeta Zero Sieve")
    parser.add_argument("--mode", choices=["run", "verify"], default="run", help="Choose operation mode (default: run)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Load the sieve parameters
    try:
        params = load_parameters(PARAMETERS_FILE)
        amplitude = params["Amplitude"]
        frequency = params["Frequency"]
        sigma = params["Smoothing Sigma"]
        tolerance = params["Tolerance"]
        if args.verbose:
            print(f"Loaded Sieve Parameters:\nAmplitude = {amplitude}\nFrequency = {frequency}\nSigma = {sigma}\nTolerance = {tolerance}\n")
    except Exception as e:
        print(f"Error loading parameters: {e}")
        return

    # Load the necessary data files
    try:
        delta_curve = np.load(DELTA_CURVE_FILE)
        dynamic_sine_envelope = np.load(DYNAMIC_SINE_ENVELOPE_FILE)
        within_band_mask = np.load(WITHIN_BAND_MASK_FILE)
        zeta_zeros = np.load(ZETA_ZEROS_FILE)
        if args.verbose:
            print(f"Loaded Data Files:\nDelta Curve: {delta_curve.shape}\nDynamic Sine Envelope: {dynamic_sine_envelope.shape}\nWithin Band Mask: {within_band_mask.shape}\nZeta Zeros: {zeta_zeros.shape}\n")
    except Exception as e:
        print(f"Error loading data files: {e}")
        return

    # Run the sieve
    if args.mode == "run":
        try:
            true_positives, false_negatives, false_positives = run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, amplitude, frequency, sigma, tolerance)
            print("\n🗸 Sieve Run Complete")
            print(f"True Positives: {len(true_positives)}")
            print(f"False Negatives: {len(false_negatives)}")
            print(f"False Positives: {len(false_positives)}")
        except Exception as e:
            print(f"Error running sieve: {e}")
    elif args.mode == "verify":
        print("\n🗸 Verification Mode (Coming Soon)")

if __name__ == "__main__":
    main()
