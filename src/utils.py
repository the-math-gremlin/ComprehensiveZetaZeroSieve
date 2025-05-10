import numpy as np
import config
from scipy.ndimage import gaussian_filter1d

def calculate_modular_drift(t_values):
    # Core drift function using theoretical base frequency
    mu_t = (2 * np.pi * config.BASE_FREQUENCY * np.log(t_values + 1)) / np.log(3)
    return mu_t

def calculate_dynamic_envelope(t_values):
    amplitude = config.AMPLITUDE * config.ENVELOPE_SCALING_FACTOR
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    smoothing_sigma = config.SMOOTHING_SIGMA
    
    # Calculate the raw sine wave
    raw_sine = amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift)
    
    # Apply Gaussian smoothing to get the local mean (mu_t)
    mu_t = gaussian_filter1d(raw_sine, sigma=smoothing_sigma)
    
    # Calculate the dynamic envelope
    envelope = np.abs(mu_t) + np.abs(amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift))
    
    # Second layer of smoothing for stability
    if smoothing_sigma > 0:
        envelope = gaussian_filter1d(envelope, sigma=smoothing_sigma)
    
    return envelope
