import os

# Base directory for data files
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

# Paths to core data files
PARAMETERS_FILE = os.path.join(DATA_DIR, "sieve_parameters.txt")
DELTA_CURVE_FILE = os.path.join(DATA_DIR, "delta_curve.npy")
DYNAMIC_SINE_ENVELOPE_FILE = os.path.join(DATA_DIR, "dynamic_sine_envelope.npy")
WITHIN_BAND_MASK_FILE = os.path.join(DATA_DIR, "within_band_mask.npy")
ZETA_ZEROS_FILE = os.path.join(DATA_DIR, "zeta_zeros.npy")

# Default parameters (used if the parameter file is missing or corrupted)
DEFAULT_PARAMETERS = {
    "Amplitude": 12.2,
    "Frequency": 0.001,
    "Smoothing_Sigma": 5.0,
    "Tolerance": 0.875,
}
