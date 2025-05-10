import numpy as np
import config

def calculate_modular_drift(t_values):
    # Core drift function using theoretical base frequency
    mu_t = (2 * np.pi * config.BASE_FREQUENCY * np.log(t_values + 1)) / np.log(3)
    return mu_t

def calculate_envelope(t_values):
    # Theoretical envelope calculation
    amplitude = config.AMPLITUDE
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    
    # Direct sine envelope calculation
    envelope = amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift)
    
    # Center the envelope
    envelope += amplitude / 2
    
    return envelope
