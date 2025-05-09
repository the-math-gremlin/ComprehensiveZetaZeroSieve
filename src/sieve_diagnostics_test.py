import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath('./src'))
from utils import load_parameters


def load_data_files():
    data_dir = os.path.abspath('../data')
    delta_curve = np.load(os.path.join(data_dir, 'delta_curve.npy'))
    dynamic_sine_envelope = np.load(os.path.join(data_dir, 'dynamic_sine_envelope.npy'))
    within_band_mask = np.load(os.path.join(data_dir, 'within_band_mask.npy'))
    zeta_zeros = np.load(os.path.join(data_dir, 'zeta_zeros.npy'))
    return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros

    delta_curve = np.load('./data/delta_curve.npy')
    dynamic_sine_envelope = np.load('./data/dynamic_sine_envelope.npy')
    within_band_mask = np.load('./data/within_band_mask.npy')
    zeta_zeros = np.load('./data/zeta_zeros.npy')
    return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros

import sys
import os
import sys
sys.path.insert(0, os.path.abspath('./src'))
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
    tolerance_radius = int(np.ceil(parameters["Tolerance"] * 10))
    known_zero_indices = set(np.round(zeta_zeros * 1000000).astype(int))
    print(f"[INFO] Loaded {len(known_zero_indices)} known zero indices (after rounding)")

    # Run the sieve in diagnostic mode
    true_positives, false_negatives, false_positives, missed_zeros = run_sieve(
        delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros, parameters, limit=None, verbose=True
    )

    # Sanity check: ensure known_zero_indices is populated
    assert len(known_zero_indices) == 100000, f"Expected 100,000 known zeros, got {len(known_zero_indices)}"

    # Check if any known zeros were missed
    missing = []
    for zero in known_zero_indices:
        if zero not in known_zero_indices:
            if debug_mode:
                print(f"[DEBUG] Zero {zero} not in known_zero_indices after rounding")
            if debug_mode:
                print(f"[DEBUG] Potential missed zero at index {zero}")
            missing.append(zero)
    print(f"Known Zeros Not Detected: {len(missing)}")
    if debug_mode:
        print(f"[DEBUG] First 10 missing zeros: {missing[:10]}")
    print(f"Missed Zero Indices: {missing}")

    # Summary
    print(f"True Positives: {true_positives}")
    print(f"False Negatives: {false_negatives}")
    print(f"False Positives: {false_positives}")
    print(f"Missed Zeros: {len(missed_zeros)}")


if __name__ == "__main__":
    test_zero_proximity_check(debug_mode=True)
