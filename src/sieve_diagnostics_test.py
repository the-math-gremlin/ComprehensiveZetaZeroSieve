import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath('./src'))
from utils import load_parameters
from main import run_sieve

def load_data_files():
    delta_curve = np.load('./data/delta_curve.npy')
    dynamic_sine_envelope = np.load('./data/dynamic_sine_envelope.npy')
    within_band_mask = np.load('./data/within_band_mask.npy')
    zeta_zeros = np.load('./data/zeta_zeros.npy')
    return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros


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

    # Sanity check: ensure zeta_zeros is populated
    assert len(known_zeros) == 100000, f"Expected 100,000 known zeros, got {len(known_zeros)}" f"Consider checking the scaling logic or data precision."

    # Check if any known zeros were missed
    missing = []
    tolerance_radius = parameters["Tolerance"]
    missed_count = 0
    for zero in zeta_zeros:
        if not np.any(np.abs(known_zeros - zero) <= tolerance_radius):
            if debug_mode and missed_count < 10:
                offsets = np.abs(known_zeros - zero)
                min_offset = np.min(offsets)
                print(f"[DEBUG] Potential missed zero at index {zero:.12f}, minimum offset: {min_offset:.12f}")
                missed_count += 1
            missing.append(zero)

    # Summary
    print(f"True Positives: {true_positives}")
    print(f"False Negatives: {false_negatives}")
    print(f"False Positives: {false_positives}")
    print(f"Missed Zeros: {len(missed_zeros)}")


if __name__ == "__main__":
    test_zero_proximity_check(debug_mode=True)
