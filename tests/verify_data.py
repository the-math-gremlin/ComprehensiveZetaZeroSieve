import os
import numpy as np
from config import DELTA_CURVE_FILE, DYNAMIC_SINE_ENVELOPE_FILE, WITHIN_BAND_MASK_FILE, ZETA_ZEROS_FILE

def verify_data():
    try:
        # Check that all files exist
        for file in [DELTA_CURVE_FILE, DYNAMIC_SINE_ENVELOPE_FILE, WITHIN_BAND_MASK_FILE, ZETA_ZEROS_FILE]:
            if not os.path.isfile(file):
                print(f"[ERROR] Missing file: {file}")
                return False

        # Load the data
        delta_curve = np.load(DELTA_CURVE_FILE)
        dynamic_sine_envelope = np.load(DYNAMIC_SINE_ENVELOPE_FILE)
        within_band_mask = np.load(WITHIN_BAND_MASK_FILE)
        zeta_zeros = np.load(ZETA_ZEROS_FILE)

        # Check for shape consistency
        if delta_curve.shape != dynamic_sine_envelope.shape:
            print("[ERROR] Delta curve and dynamic sine envelope shapes do not match.")
            print(f"Delta Curve: {delta_curve.shape}, Dynamic Sine Envelope: {dynamic_sine_envelope.shape}")
            return False

        if len(within_band_mask) != len(delta_curve):
            print("[ERROR] Within band mask length does not match delta curve length.")
            print(f"Within Band Mask: {len(within_band_mask)}, Delta Curve: {len(delta_curve)}")
            return False

        # Check for valid zero values
        if np.any(zeta_zeros < 0):
            print("[ERROR] Zeta zeros contain negative values, which is not allowed.")
            print(f"Min Zero: {np.min(zeta_zeros)}")
            return False

        # Check for correct data types
        if not all(isinstance(x, (int, float)) for x in zeta_zeros):
            print("[ERROR] Zeta zeros contain non-numeric values.")
            return False

        # Summary report
        print("[INFO] All data files are correctly formatted and aligned.")
        print(f"Delta Curve Length: {len(delta_curve)}")
        print(f"Within Band Mask Length: {len(within_band_mask)}")
        print(f"Number of Known Zeros: {len(zeta_zeros)}")
        return True

    except Exception as e:
        print(f"[ERROR] Unexpected error while verifying data: {e}")
        return False


if __name__ == "__main__":
    verify_data()
