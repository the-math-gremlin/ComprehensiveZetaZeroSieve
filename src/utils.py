import numpy as np
from config import PARAMETERS_FILE, DEFAULT_PARAMETERS

def load_data_files():
    """Load the main data files for the sieve."""
    try:
        delta_curve = np.load("../data/delta_curve.npy")
        dynamic_sine_envelope = np.load("../data/dynamic_sine_envelope.npy")
        within_band_mask = np.load("../data/within_band_mask.npy")
        zeta_zeros = np.load("../data/zeta_zeros.npy")
        return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros
    except FileNotFoundError as e:
        print(f"[ERROR] Missing data file: {e.filename}")
        raise

    return parameters

def load_data_files():
    """Load the main data files for the sieve."""
    delta_curve = np.load("../data/delta_curve.npy")
    dynamic_sine_envelope = np.load("../data/dynamic_sine_envelope.npy")
    within_band_mask = np.load("../data/within_band_mask.npy")
    zeta_zeros = np.load("../data/zeta_zeros.npy")
    return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros
