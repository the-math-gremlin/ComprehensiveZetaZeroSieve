import numpy as np
import config

def calculate_modular_drift(t_values):
    # Calculate the modular drift function (Δ)
    frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    mu_t = (2 * np.pi * frequency * np.log(t_values + 1)) / np.log(3) + phase_shift
    delta_curve = np.abs(np.mod(mu_t, 2 * np.pi) - np.pi)
    return delta_curve

def calculate_envelope(t_values):
    amplitude = config.AMPLITUDE
    frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    
    # Calculate the base sine envelope
    sine_wave = amplitude * np.sin(frequency * np.log(t_values + 1) + phase_shift)
    
    # Center the envelope correctly around the target mean
    mu_t = (2 * np.pi * frequency * np.log(t_values + 1)) / np.log(3)
    envelope = np.abs(mu_t + sine_wave)
    
    return envelope

def run_sieve(t_values, delta_curve, envelope, tolerance):
    # Identify points where Δ is within the envelope
    detected_zeros = t_values[np.abs(delta_curve) < envelope + tolerance]
    return detected_zeros
