import numpy as np

# Core sieve parameters (theoretical)
AMPLITUDE = np.pi * abs(1 / np.log(3) - 1 / np.log(np.pi)) / 2  # ≈ 2.282
BASE_FREQUENCY = abs(1 / np.log(3) - 1 / np.log(np.pi))  # ≈ 0.001542
SMOOTHING_SIGMA = 5.0
TOLERANCE = 0.875
PHASE_SHIFT = 0.0

# t-value generation
MIN_T = 14.134725  # Start at the first known zero
MAX_T = 100000.0   # Adjust as needed
NUM_POINTS = 100000
