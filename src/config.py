DELTA_CURVE_FILE = "../data/delta_curve.npy"
DYNAMIC_SINE_ENVELOPE_FILE = "../data/dynamic_sine_envelope.npy"
WITHIN_BAND_MASK_FILE = "../data/within_band_mask.npy"
KNOWN_ZEROS_FILE = "../data/zeta_zeros.npy"

# Sieve Parameters
AMPLITUDE = np.pi * np.abs(1 / np.log(3) - 1 / np.log(np.pi))
FREQUENCY = np.abs(1 / np.log(3) - 1 / np.log(np.pi))
PHASE_SHIFT = 0.0
SMOOTHING_SIGMA = 50
TOLERANCE = 0.875
