import numpy as np
import config
import os

def verify_zeros(detected_zeros):
    known_zeros = np.load(config.KNOWN_ZEROS_FILE)
    
    # Ensure both are int64
    detected_zeros = np.array(detected_zeros, dtype=np.int64)
    known_zeros = np.array(known_zeros, dtype=np.int64)
    
    # Diagnostic output
    print("=== Zero Comparison Diagnostic ===")
    print(f"First 20 detected zeros: {detected_zeros[:20]}")
    print(f"First 20 known zeros: {known_zeros[:20]}")
    
    matches = np.isin(detected_zeros, known_zeros)
    true_positives = np.sum(matches)
    false_positives = len(detected_zeros) - true_positives
    missed_zeros = len(known_zeros) - true_positives
    
    print(f"[INFO] True Positives: {true_positives}")
    print(f"[INFO] False Positives: {false_positives}")
    print(f"[INFO] Missed Zeros: {missed_zeros}")

if __name__ == "__main__":
    detected_zeros_path = os.path.join("..", "data", "detected_zeros.npy")
    detected_zeros = np.load(detected_zeros_path)
    verify_zeros(detected_zeros)
