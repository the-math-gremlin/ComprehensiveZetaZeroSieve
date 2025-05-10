import numpy as np
import config
from scipy.ndimage import gaussian_filter1d

def calculate_modular_drift(t_values):
    # Core drift function using theoretical base frequency
    mu_t = (2 * np.pi * config.BASE_FREQUENCY * np.log(t_values + 1)) / np.log(3)
    return mu_t

def calculate_envelope(t_values):
    amplitude = config.AMPLITUDE
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    
    # Direct sine envelope calculation
    sine_wave = amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift)
    
    # Center the envelope around the mean of the sine wave
    envelope = sine_wave + (amplitude / 2)
    
    # Optional smoothing
    if config.SMOOTHING_SIGMA > 0:
        envelope = gaussian_filter1d(envelope, sigma=config.SMOOTHING_SIGMA)
    
    return envelope

def run_sieve(t_values, delta_curve, envelope, tolerance):
    # Run the sieve to identify potential zeros
    detected_zeros = []
    for t, delta, env in zip(t_values, delta_curve, envelope):
        if abs(delta) <= tolerance * abs(env):
            detected_zeros.append(t)
    return detected_zeros
