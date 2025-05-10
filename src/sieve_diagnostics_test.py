import numpy as np
from utils import load_parameters, load_data_files
from main import run_sieve

def verify_zeros(detected_zeros, zeta_zeros, tolerance=1e-8):
    """
    Verify that all detected zeros are actual known zeros.
    """
    matched_zeros = []
    false_positives = []

    for zero in detected_zeros:
        if np.any(np.isclose(zero, zeta_zeros, rtol=1e-12, atol=tolerance)):
            matched_zeros.append(zero)
        else:
            false_positives.append(zero)

    return matched_zeros, false_positives


if __name__ == "__main__":
    # Load data
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    t_values = np.arange(1, len(delta_curve) + 1, dtype=np.float64)

    # Run the sieve independently of known zeros
    detected_zeros = run_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, parameters, t_values=t_values, limit=None, verbose=True)

    # Verify the detected zeros
    matched_zeros, false_positives = verify_zeros(detected_zeros, zeta_zeros)

    # Print summary
    print("\n=== Verification Results ===")
    print(f"Detected Zeros: {len(detected_zeros)}")
    print(f"Matched Zeros: {len(matched_zeros)}")
    print(f"False Positives: {len(false_positives)}")
    print(f"First 20 False Positives: {false_positives[:20]}\n")
