import numpy as np
import config
from scipy.ndimage import gaussian_filter1d

def calculate_modular_drift(t_values):
    # Core drift function using theoretical base frequency
    mu_t = (2 * np.pi * config.BASE_FREQUENCY * np.log(t_values + 1)) / np.log(3)
    return mu_t

def calculate_envelope(t_values):
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    smoothing_sigma = config.SMOOTHING_SIGMA
    
    # Calculate a rough local amplitude estimate
    raw_sine = np.sin(base_frequency * np.log(t_values + 1) + phase_shift)
    local_amplitude = np.max(np.abs(raw_sine))
    
    # Calculate the local mean (mu_t)
    mu_t = gaussian_filter1d(raw_sine, sigma=smoothing_sigma)
    
    # Scale the envelope dynamically
    envelope = mu_t + (local_amplitude * raw_sine)
    
    # Apply a second layer of smoothing for stability
    if smoothing_sigma > 0:
        envelope = gaussian_filter1d(envelope, sigma=smoothing_sigma)
    
    return np.abs(envelope)

def run_sieve(t_values, delta_curve, envelope, tolerance):
    # Run the sieve to identify potential zeros
    detected_zeros = []
    for t, delta, env in zip(t_values, delta_curve, envelope):
        if abs(delta) <= tolerance * abs(env):
            detected_zeros.append(t)
    return detected_zeros
