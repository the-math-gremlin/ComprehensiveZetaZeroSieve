import numpy as np

# Core sieve parameters
AMPLITUDE = np.pi * abs(1 / np.log(3) - 1 / np.log(np.pi)) / 2
BASE_FREQUENCY = abs(1 / np.log(3) - 1 / np.log(np.pi))
SMOOTHING_SIGMA = 5.0
TOLERANCE = 0.875
PHASE_SHIFT = 0.0

# t-value generation
MIN_T = 10  # Start at the first known zero
MAX_T = 100000.0   # Adjust as needed
NUM_POINTS = 100000
