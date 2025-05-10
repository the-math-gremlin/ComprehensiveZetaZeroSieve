import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Updated parameters from the sieve file
A = 12.2  # Amplitude
f = 0.001  # Frequency
sigma = 5.0  # Smoothing Sigma
epsilon = 0.875  # Tolerance

# Load the validated preprocessed data
smoothed_delta = np.load('/mnt/data/smoothed_delta.npy')
delta_curve = np.load('/mnt/data/delta_curve.npy')
dynamic_sine_envelope = np.load('/mnt/data/dynamic_sine_envelope.npy')
within_band_mask = np.load('/mnt/data/within_band_mask.npy')
zeta_zeros = np.load('/mnt/data/zeta_zeros.npy')

t_min, t_max = 50, 1000
num_points = delta_curve.shape[0]
t_values = np.linspace(t_min, t_max, num_points)


def plot_validated_sieve():
    # Plotting the validated sieve data
    plt.figure(figsize=(14, 8))
    plt.plot(t_values, delta_curve, label="$\Delta(t)$ - Modular Drift", color="blue", alpha=0.7)
    plt.plot(t_values, smoothed_delta, label="$\mu(t)$ - Smoothed Centerline", color="green", alpha=0.6, linestyle='--')
    plt.plot(t_values, dynamic_sine_envelope, label="$E_-(t)$ - Harmonic Envelope", color="orange", alpha=0.7)
    plt.scatter(t_values[within_band_mask], delta_curve[within_band_mask], color="red", label="Sieve Zero Candidates", s=10)
    plt.title("Modular Drift and Harmonic Envelope (Loaded Data)")
    plt.xlabel("t")
    plt.ylabel("Modular Drift (radians)")
    plt.legend()
    plt.show()
    
    # Return the detected zero locations
    return t_values[within_band_mask]


# Run the validated sieve plot
candidate_zeros = plot_validated_sieve()
len(candidate_zeros), candidate_zeros[:10]  # Show the first 10 detected zeros as a sanity check
