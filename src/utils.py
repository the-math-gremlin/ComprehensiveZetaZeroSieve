import numpy as np
from config import PARAMETERS_FILE, DEFAULT_PARAMETERS

def load_parameters():
    """Load sieve parameters from the configuration file."""
    parameters = DEFAULT_PARAMETERS.copy()

    try:
        with open(PARAMETERS_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.strip().split(":")
                    key, value = key.strip(), value.strip()
                    if key in parameters:
                        parameters[key] = float(value)
    except FileNotFoundError:
        print(f"[Warning] Parameter file '{PARAMETERS_FILE}' not found. Using default parameters.")

    return parameters

def load_data_files():
    """Load the main data files for the sieve."""
    delta_curve = np.load("../data/delta_curve.npy")
    dynamic_sine_envelope = np.load("../data/dynamic_sine_envelope.npy")
    within_band_mask = np.load("../data/within_band_mask.npy")
    zeta_zeros = np.load("../data/zeta_zeros.npy")
    return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros
