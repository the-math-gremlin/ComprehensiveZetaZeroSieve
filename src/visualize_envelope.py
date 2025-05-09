import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from config import DELTA_CURVE_FILE, DYNAMIC_SINE_ENVELOPE_FILE, ZETA_ZEROS_FILE, PARAMETERS_FILE
from utils import load_parameters

def visualize_envelope():
    # Load data
    delta_curve = np.load(DELTA_CURVE_FILE)
    known_zeros = np.load(ZETA_ZEROS_FILE)
    params = load_parameters(PARAMETERS_FILE)

    # Extract parameters
    A = params["Amplitude"]
    f = params["Frequency"]
    sigma = params["Smoothing_Sigma"]

    # Calculate the smoothed centerline (mu_t)
    mu_t = gaussian_filter1d(delta_curve, sigma)

    # Reconstruct the dynamic sine envelope
    t_values = np.arange(1, len(delta_curve) + 1)
    envelope_reconstructed = mu_t + A * np.sin(2 * np.pi * f * np.log(t_values + 1))

    # Plot the delta curve
    plt.figure(figsize=(14, 8))
    plt.plot(t_values, delta_curve, color='blue', label='Delta Curve (Raw)')
    plt.plot(t_values, mu_t, color='green', linestyle='--', linewidth=2, label='Smoothed Centerline (mu_t)')
    plt.plot(t_values, envelope_reconstructed, color='red', linewidth=1.5, label='Reconstructed Envelope')

    # Highlight known zeros
    zero_indices = [int(round(z)) for z in known_zeros if z < len(delta_curve)]
    plt.scatter(zero_indices, envelope_reconstructed[zero_indices], color='orange', marker='x', s=50, label='Known Zeros')

    # Add labels and legend
    plt.title("Reconstructed Envelope vs Delta Curve")
    plt.xlabel("Index (t)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    visualize_envelope()
