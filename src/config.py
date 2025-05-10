import numpy as np

# Parameter file path
PARAMETERS_FILE = "../data/sieve_parameters.txt"

# Data file paths
DELTA_CURVE_FILE = "../data/delta_curve.npy"
DYNAMIC_SINE_ENVELOPE_FILE = "../data/dynamic_sine_envelope.npy"
WITHIN_BAND_MASK_FILE = "../data/within_band_mask.npy"
ZETA_ZEROS_FILE = "../data/zeta_zeros.npy"

# Default parameters for the sieve
DEFAULT_PARAMETERS = {
    "Amplitude": np.pi * abs(1 / np.log(3) - 1 / np.log(np.pi)) / 2,
    "Frequency": 0.001,
    "Smoothing_Sigma": 5.0,
    "Tolerance": 0.875,
    "Phase_Shift": 0.0,
    "Seed_Region_End": 50,
    "Base_Frequency": abs(1 / np.log(3) - 1 / np.log(np.pi))
}
