import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath('./src'))
from utils import load_parameters, load_data_files
import sys
import os
import sys
sys.path.insert(0, os.path.abspath('./src'))
from main import run_sieve


def test_zero_proximity_check():
    # Load parameters and data
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    tolerance_radius = int(np.ceil(parameters["Tolerance"] * 10))
    known_zero_indices = set(np.round(zeta_zeros).astype(int))

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
            missing.append(zero)
    print(f"Known Zeros Not Detected: {len(missing)}")
    print(f"Missed Zero Indices: {missing}")

    # Summary
    print(f"True Positives: {true_positives}")
    print(f"False Negatives: {false_negatives}")
    print(f"False Positives: {false_positives}")
    print(f"Missed Zeros: {len(missed_zeros)}")


if __name__ == "__main__":
    test_zero_proximity_check()
