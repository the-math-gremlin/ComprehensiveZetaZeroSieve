import numpy as np
from utils import load_data, run_basic_sieve
import config

def main():
    print("[INFO] Loading data files...")
    delta_curve, dynamic_sine_envelope, within_band_mask = load_data()
    print("[INFO] Running basic sieve...")
    detected_zeros = run_basic_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, verbose=True)
    print(f"[INFO] Detected {len(detected_zeros)} potential zeros.")
    print("[INFO] Sieve complete.")

if __name__ == "__main__":
    main()
