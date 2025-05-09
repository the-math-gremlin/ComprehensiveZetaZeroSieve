import numpy as np

# Core sieve parameters
AMPLITUDE = np.pi * abs(1 / np.log(3) - 1 / np.log(np.pi)) / 2
BASE_FREQUENCY = abs(1 / np.log(3) - 1 / np.log(np.pi))
SMOOTHING_SIGMA = 5.0
TOLERANCE = 0.875
PHASE_SHIFT = 0.0

# t-value generation
MIN_T = 0.0
MAX_T = 100000.0
NUM_POINTS = 100000

# Envelope scaling (dynamic adjustment)
ENVELOPE_SCALING_FACTOR = 2.0  # Adjust this as needed
