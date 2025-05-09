import numpy as np
import os
from config import PARAMETERS_FILE, DELTA_CURVE_FILE, DYNAMIC_SINE_ENVELOPE_FILE, WITHIN_BAND_MASK_FILE, ZETA_ZEROS_FILE, DEFAULT_PARAMETERS

def load_parameters(file_path=PARAMETERS_FILE):
    parameters = DEFAULT_PARAMETERS.copy()
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if ":" in line:
                    key, value = line.strip().split(":")
                    parameters[key.strip()] = float(value.strip())
    return parameters

def load_data_files():
    delta_curve = np.load(DELTA_CURVE_FILE)
    dynamic_sine_envelope = np.load(DYNAMIC_SINE_ENVELOPE_FILE)
    within_band_mask = np.load(WITHIN_BAND_MASK_FILE)
    zeta_zeros = np.load(ZETA_ZEROS_FILE)
    return delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros
