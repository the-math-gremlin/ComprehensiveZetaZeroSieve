import os
import numpy as np
import argparse
from sieve import run_sieve
from utils import load_parameters
import config

def main():
    parser = argparse.ArgumentParser(description="Comprehensive Zeta Zero Sieve")
    parser.add_argument("--mode", choices=["run", "verify"], default="run", help="Choose operation mode (default: run)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Load parameters
    try:
        params = load_parameters(config.PARAMETERS_FILE)
        amplitude = params["Amplitude"]
        frequency = params["Frequency"]
        sigma = params["Smoothing_Sigma"]
        tolerance = params["Tolerance"]
        if args.verbose:
            print(f"Loaded Sieve Parameters:\nAmplitude = {amplitude}\nFrequency = {frequency}\nSigma = {sigma}\nTolerance = {tolerance}\n")
    except Exception as e:
        print(f"Error loading parameters: {e}")
        return

    # Load core data files
    try:
        delta_curve = np.load(config.DELTA_CURVE_FILE)
        dynamic_sine_envelope = np.load(config.DYNAMIC_SINE_ENVELOPE_FILE)
        within_band_mask = np.load(config.WITHIN_BAND_MASK_FILE)
        zeta_zeros = np.load(config.ZETA_ZEROS_FILE)
        if args.verbose:
            print(f"Loaded Data Files:\nDelta Curve: {delta_curve.shape}\nDynamic Sine Envelope: {dynamic_sine_envelope.shape}\nWithin Band Mask: {within_band_mask.shape}\nZeta Zeros: {zeta_zeros.shape}\n")
    except Exception as e:
        print(f"Error loading data files: {e}")
        return
    # Data check
    if delta_curve.shape != dynamic_sine_envelope.shape or len(within_band_mask) != len(delta_curve):
    print("Error: Data files are not correctly aligned.")
    return

    # Run the sieve
try:
    results = run_sieve(params, delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros)
    if args.verbose:
        for key, value in results.items():
            print(f"{key}: {len(value)}")
except Exception as e:
    print(f"Error running sieve: {e}")


if __name__ == "__main__":
    main()
