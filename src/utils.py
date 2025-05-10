import numpy as np
from scipy.ndimage import gaussian_filter1d

def calculate_modular_drift(t_values):
    """
    Calculate the modular drift function Δ(t) based on the logarithmic spiral alignment.
    """
    # Calculate the base-3 and base-pi phases
    theta_3 = 2 * np.pi * (np.log(t_values) / np.log(3) % 1)
    theta_pi = 2 * np.pi * (np.log(t_values) / np.log(np.pi) % 1)

    # Calculate the absolute phase difference
    delta_theta = np.abs(theta_3 - theta_pi)

    # Correct for the periodic boundary condition
    delta = np.minimum(delta_theta, 2 * np.pi - delta_theta)

    return delta.astype(np.float64)

def calculate_envelope(delta_curve, t_values, amplitude, frequency, phase_shift, b0=3, smoothing_sigma=50):
    """
    Calculate the harmonic envelope with a smoothed centerline μ(t).
    """
    # Calculate the smoothed centerline
    mu_t = gaussian_filter1d(delta_curve, sigma=smoothing_sigma)

    # Calculate the envelope
    envelope = mu_t + amplitude * np.sin(
        (2 * np.pi * frequency * np.log(t_values + 1) / np.log(b0)) + phase_shift
    )

    return envelope.astype(np.float64), mu_t.astype(np.float64)
