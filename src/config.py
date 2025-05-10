import numpy as np

# Core sieve parameters
BASE_FREQUENCY = np.pi
PHASE_SHIFT = 0
AMPLITUDE = np.pi * np.abs(1 / np.log(3) - 1 / np.log(np.pi))
ENVELOPE_FREQUENCY = 0.5
TOLERANCE = 0.01

# t-value generation
MIN_T = 14.0
MAX_T = 100000.0
NUM_POINTS = 100000
