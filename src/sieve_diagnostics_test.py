import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath('./src'))
from utils import load_parameters, load_data_files
from main import run_sieve

def test_zero_proximity_check(debug_mode=False):
    # Load parameters and data
    parameters = load_parameters()
    parameters_file = os.path.abspath('../data/sieve_parameters.txt')
    if os.path.exists(parameters_file):
        print(f"[INFO] Loading parameters from {parameters_file}")
    else:
        print("[WARNING] Parameter file '../data/sieve_parameters.txt' not found. Using default parameters.")
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    tolerance_radius = parameters["Tolerance"]
    print(f"[INFO] Using floating point tolerance of {tolerance_radius}")
    known_zeros = np.array(zeta_zeros, dtype=np.float64)
    print(f"[INFO] Loaded {len(known_zeros)} known zeros for direct precision matching")

    # Run the sieve in diagnostic mode
    true_positives, false_negatives, false_positives, missed_zeros = run_sieve(
        delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None, verbose=True
    )

    # Print the summary in the correct format for parameter_sweep.py
    print(f"True Positives: {true_positives}")
    print(f"False Positives: {false_positives}")
    print(f"Missed Zeros: {len(missed_zeros)}")

if __name__ == "__main__":
    test_zero_proximity_check(debug_mode=True)
