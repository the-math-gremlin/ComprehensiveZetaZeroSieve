import numpy as np

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
