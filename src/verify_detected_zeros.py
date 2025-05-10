import numpy as np

def verify_detected_zeros(detected_file="../data/detected_zeros.npy", known_file="../data/zeta_zeros.npy"):
    # Load the detected and known zeros
    detected_zeros = np.load(detected_file)
    zeta_zeros = np.load(known_file)

    # Sort for direct comparison
    detected_zeros = np.sort(detected_zeros)
    zeta_zeros = np.sort(zeta_zeros)

    # Check for matches
    true_positives = np.intersect1d(detected_zeros, zeta_zeros)
    false_positives = np.setdiff1d(detected_zeros, zeta_zeros)
    missed_zeros = np.setdiff1d(zeta_zeros, detected_zeros)

    # Print summary
    print("\n=== Zero Verification Summary ===")
    print(f"Total Detected Zeros: {len(detected_zeros)}")
    print(f"Total Known Zeros: {len(zeta_zeros)}")
    print(f"True Positives: {len(true_positives)}")
    print(f"False Positives: {len(false_positives)}")
    print(f"Missed Zeros: {len(missed_zeros)}")
    
    if len(false_positives) == 0 and len(missed_zeros) == 0:
        print("\n[INFO] All detected zeros match the known zeros. Sieve is functioning correctly.")
    else:
        print("\n[WARNING] Mismatches detected. Please review the false positives and missed zeros.")
        print(f"\nFalse Positives: {false_positives[:20]}")
        print(f"Missed Zeros: {missed_zeros[:20]}")

if __name__ == "__main__":
    verify_detected_zeros()
