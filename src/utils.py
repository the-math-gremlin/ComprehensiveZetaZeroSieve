import numpy as np
import config
from scipy.ndimage import gaussian_filter1d

def calculate_modular_drift(t_values):
    # Core drift function using theoretical base frequency
    mu_t = (2 * np.pi * config.BASE_FREQUENCY * np.log(t_values + 1)) / np.log(3)
    return mu_t

def calculate_dynamic_envelope(t_values):
    amplitude = config.AMPLITUDE
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    smoothing_sigma = config.SMOOTHING_SIGMA
    
    # Calculate the local mean (mu_t) using a Gaussian filter for dynamic centering
    raw_sine = amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift)
    mu_t = gaussian_filter1d(raw_sine, sigma=smoothing_sigma)
    
    # Scale the envelope dynamically
    dynamic_envelope = mu_t + (amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift))
    
    # Apply a second layer of smoothing for stability
    if smoothing_sigma > 0:
        dynamic_envelope = gaussian_filter1d(dynamic_envelope, sigma=smoothing_sigma)
    
    return np.abs(dynamic_envelope)

def run_sieve(t_values, delta_curve, envelope, tolerance):
    # Run the sieve to identify potential zeros
    detected_zeros = []
    for t, delta, env in zip(t_values, delta_curve, envelope):
        if abs(delta) <= tolerance * abs(env):
            detected_zeros.append(t)
    return detected_zeros
