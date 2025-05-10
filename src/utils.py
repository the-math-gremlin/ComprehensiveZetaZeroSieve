import numpy as np
import config

def calculate_modular_drift(t_values):
    # Calculate the drift component using the corrected base frequency
    mu_t = (2 * np.pi * config.BASE_FREQUENCY * np.log(t_values + 1)) / np.log(3) + config.PHASE_SHIFT
    return mu_t

def calculate_envelope(t_values):
    # Calculate the envelope using the corrected amplitude and base frequency
    mu_t = calculate_modular_drift(t_values)
    envelope = mu_t + config.AMPLITUDE * np.sin(config.BASE_FREQUENCY * np.log(t_values + 1) + config.PHASE_SHIFT)
    return envelope

def run_sieve(t_values, delta_curve, envelope):
    # Run the sieve to identify potential zeros
    detected_zeros = []
    for t, delta, env in zip(t_values, delta_curve, envelope):
        if abs(delta - env) <= config.TOLERANCE:
            detected_zeros.append(t)
    return detected_zeros
