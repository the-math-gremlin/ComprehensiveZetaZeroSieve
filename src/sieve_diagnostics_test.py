import numpy as np
import config
import os

def verify_zeros(detected_zeros):
    known_zeros = np.load(config.KNOWN_ZEROS_FILE)
    matches = [z for z in detected_zeros if z in known_zeros]
    print(f"[INFO] True Positives: {len(matches)}")
    print(f"[INFO] Missed Zeros: {len(known_zeros) - len(matches)}")
    print(f"[INFO] False Positives: {len(detected_zeros) - len(matches)}")

if __name__ == "__main__":
    detected_zeros_path = os.path.join("..", "data", "detected_zeros.npy")
    detected_zeros = np.load(detected_zeros_path)
    verify_zeros(detected_zeros)
