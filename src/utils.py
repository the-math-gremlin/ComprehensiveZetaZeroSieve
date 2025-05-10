import numpy as np
import config

def calculate_modular_drift(t_values):
    base_frequency = config.BASE_FREQUENCY
    phase_shift = config.PHASE_SHIFT
    mu_t = (2 * np.pi * base_frequency * np.log(t_values + 1)) / np.log(3) + phase_shift
    return mu_t

def calculate_envelope(t_values):
    amplitude = config.AMPLITUDE
    base_frequency = config.BASE_FREQUENCY
    smoothing_sigma = config.SMOOTHING_SIGMA
    phase_shift = config.PHASE_SHIFT
    
    # Core sine wave component
    sine_wave = amplitude * np.sin(base_frequency * np.log(t_values + 1) + phase_shift)
    
    # Dynamic envelope scaling
    envelope_base = amplitude / 1.5  # Base scaling factor
    envelope_adjusted = envelope_base + sine_wave

    # Optional smoothing to reduce noise
    if smoothing_sigma > 0:
        from scipy.ndimage import gaussian_filter1d
        envelope_adjusted = gaussian_filter1d(envelope_adjusted, sigma=smoothing_sigma)
    
    return envelope_adjusted

def run_sieve(t_values, delta_curve, envelope, tolerance):
    # Find zeros where delta is within the envelope tolerance
    detected_zeros = []
    for i, (t, delta, env) in enumerate(zip(t_values, delta_curve, envelope)):
        if abs(delta) <= tolerance * env:
            detected_zeros.append(t)
    
    return detected_zeros
