import numpy as np
import config

def calculate_modular_drift(t_values):
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    mu_t = (2 * np.pi * base_frequency * np.log(t_values + 1)) / np.log(3) + phase_shift
    return mu_t

def calculate_envelope(t_values):
    frequency = config.BASE_FREQUENCY
    amplitude = config.AMPLITUDE
    envelope = mu_t(t_values) + amplitude * np.sin(frequency * np.log(t_values + 1))
    return envelope

def run_sieve(t_values, delta_curve, envelope, tolerance):
    # Find zeros where delta is within the envelope tolerance
    detected_zeros = []
    for i, (t, delta, env) in enumerate(zip(t_values, delta_curve, envelope)):
        if abs(delta) <= tolerance * env:
            detected_zeros.append(t)
    
    return detected_zeros
