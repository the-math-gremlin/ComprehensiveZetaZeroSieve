import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.widgets import Slider

# Updated parameters from the sieve file
A = 12.2  # Amplitude
f = 0.001  # Frequency
sigma = 5.0  # Smoothing Sigma
epsilon = 0.875  # Tolerance

# Define the modular drift function without relying on preprocessed data
def modular_drift(t):
    ln3 = np.log(3)
    lnpi = np.log(np.pi)
    theta_3 = 2 * np.pi * (np.log(t) / ln3 % 1)
    theta_pi = 2 * np.pi * (np.log(t) / lnpi % 1)
    delta = np.abs(theta_3 - theta_pi)
    return np.minimum(delta, 2 * np.pi - delta)

# Define the harmonic envelope dynamically without preprocessed data
def harmonic_envelope(t, sigma=5.0):
    raw_drift = modular_drift(t)
    # Apply Gaussian smoothing for the centerline
    window = int(2 * sigma + 1)
    mu_t = np.convolve(raw_drift, np.ones(window)/window, mode='same')
    envelope = mu_t + A * np.sin(f * np.log(t+1))
    return mu_t, envelope

def plot_interactive_sieve(t_min=50, t_max=1000, num_points=10000):
    t_values = np.linspace(t_min, t_max, num_points)
    delta_t = modular_drift(t_values)
    mu_t, env_t = harmonic_envelope(t_values, sigma)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    plt.subplots_adjust(left=0.1, bottom=0.25)
    
    # Initial plot
    line_delta, = ax.plot(t_values, delta_t, label="$\Delta(t)$ - Modular Drift", color="blue", alpha=0.7)
    line_mu, = ax.plot(t_values, mu_t, label="$\mu(t)$ - Smoothed Centerline", color="green", alpha=0.6, linestyle='--')
    line_env, = ax.plot(t_values, env_t, label="$E_-(t)$ - Harmonic Envelope", color="orange", alpha=0.7)
    scatter_zeros = ax.scatter([], [], color="red", label="Sieve Zero Candidates", s=10)
    
    # Slider for adjusting tolerance
    ax_tol = plt.axes([0.1, 0.1, 0.8, 0.05], facecolor='lightgrey')
    slider_tol = Slider(ax_tol, 'Tolerance', 0.1, 2.0, valinit=epsilon, valstep=0.01)
    
    def update(val):
        tol = slider_tol.val
        mask = np.abs(delta_t - env_t) < tol
        scatter_zeros.set_offsets(np.c_[t_values[mask], delta_t[mask]])
        fig.canvas.draw_idle()
    
    slider_tol.on_changed(update)
    
    # Set plot labels and title
    ax.set_title("Modular Drift and Harmonic Envelope (Interactive)")
    ax.set_xlabel("t")
    ax.set_ylabel("Modular Drift (radians)")
    ax.legend()
    plt.show()


# Run the fully standalone interactive sieve plot
plot_interactive_sieve()
