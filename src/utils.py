import numpy as np
import os
from config import PARAMETERS_FILE, DEFAULT_PARAMETERS

def load_parameters():
    """Load sieve parameters from the configuration file."""
    parameters = DEFAULT_PARAMETERS.copy()

    try:
        with open(PARAMETERS_FILE, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=")
                    key, value = key.strip(), value.strip()
                    if key in parameters:
                        parameters[key] = float(value)
    except FileNotFoundError:
        print(f"[ERROR] Parameter file '{PARAMETERS_FILE}' not found. Using default parameters.")

    return parameters

def load_data_files():
    """Load the main data files for the sieve, ensuring float64 precision."""
    try:
        delta_curve = np.load("../data/delta_curve.npy").astype(np.float64)
        dynamic_sine_envelope = np.load("../data/dynamic_sine_envelope.npy").astype(np.float64)
        within_band_mask = np.load("../data/within_band_mask.npy").astype(np.float64)
        zeta_zeros = np.load("../data/zeta_zeros.npy").astype(np.float64)

        # Verify length consistency
        if not (len(delta_curve) == len(dynamic_sine_envelope) == len(within_band_mask)):
            raise ValueError("Data length mismatch between delta curve, envelope, and mask files.")

        print(f"[INFO] Loaded data files with {len(delta_curve)} entries each.")
        print(f"[INFO] Loaded {len(zeta_zeros)} known zeros.")

        return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros

    except FileNotFoundError as e:
        print(f"[ERROR] Missing data file: {e.filename}")
        raise
    except ValueError as e:
        print(f"[ERROR] Data length mismatch: {e}")
        raise

