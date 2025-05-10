import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
from matplotlib.widgets import Slider

# Updated parameters from the sieve file
A = 12.2  # Amplitude
f = 0.001  # Frequency
sigma = 5.0  # Smoothing Sigma
epsilon = 0.875  # Tolerance

# Load the known zeta zeros for overlay
zeta_zeros = np.load('../data/zeta_zeros.npy')

# Define the modular drift function without relying on preprocessed data
def modular_drift(t):
    ln3 = np.log(3)
    lnpi = np.log(np.pi)
    theta_3 = 2 * np.pi * (np.log(t) / ln3 % 1)
    theta_pi = 2 * np.pi * (np.log(t) / lnpi % 1)
    delta = np.abs(theta_3 - theta_pi)
    return np.minimum(delta, 2 * np.pi - delta)

# Define the harmonic envelope dynamically without preprocessed data
def harmonic_envelope(t, sigma=5.0, amplitude=12.2, frequency=0.001, phase_shift=np.pi/4):
    raw_drift = modular_drift(t)
    # Apply proper Gaussian smoothing for the centerline
    mu_t = gaussian_filter1d(raw_drift, sigma=sigma)
    # Optimized envelope with precise amplitude scaling and phase correction
    envelope = mu_t + amplitude * np.sin(frequency * np.log(t+1) + phase_shift)
    return mu_t, envelope


def plot_interactive_sieve(t_min=50, t_max=1000, num_points=100000):
    t_values = np.linspace(t_min, t_max, num_points)
    delta_t = modular_drift(t_values)
    mu_t, env_t = harmonic_envelope(t_values, sigma)
    
    fig, (ax, ax_hist) = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [3, 1]})
    plt.subplots_adjust(left=0.1, bottom=0.4)
    
    # Initial plot
    line_delta, = ax.plot(t_values, delta_t, label=r"$\Delta(t)$ - Modular Drift", color="blue", alpha=0.7)
    line_mu, = ax.plot(t_values, mu_t, label=r"$\mu(t)$ - Smoothed Centerline", color="green", alpha=0.6, linestyle='--')
    line_env, = ax.plot(t_values, env_t, label=r"$E_-(t)$ - Harmonic Envelope", color="orange", alpha=0.7)
    scatter_zeros = ax.scatter([], [], color="red", label="Sieve Zero Candidates", s=10)
    overlay_zeros = ax.scatter(zeta_zeros, np.zeros_like(zeta_zeros), color="black", label="Known Zeta Zeros", s=10, alpha=0.6)
    
    # Zero count display
    zero_count_text = ax.text(0.05, 0.95, f"Captured Zeros: 0 / 99995", transform=ax.transAxes, fontsize=12, color="black", bbox=dict(facecolor='white', alpha=0.8))
    
    # Histogram for capture efficiency
    hist_data = np.zeros(99995)
    hist_bar = ax_hist.bar(np.arange(99995), hist_data, color='skyblue')
    ax_hist.set_title("Capture Efficiency (Per Zero)")
    ax_hist.set_xlabel("Zero Index")
    ax_hist.set_ylabel("Capture Distance")
    ax_hist.set_xlim(0, 100)
    ax_hist.set_ylim(0, 2 * np.pi)
    
    # Sliders for adjusting tolerance, amplitude, and frequency
    ax_tol = plt.axes([0.1, 0.25, 0.8, 0.05], facecolor='lightgrey')
    slider_tol = Slider(ax_tol, 'Tolerance', 0.1, 2.0, valinit=epsilon, valstep=0.01)
    
    ax_amp = plt.axes([0.1, 0.15, 0.8, 0.05], facecolor='lightgrey')
    slider_amp = Slider(ax_amp, 'Amplitude', 10.0, 15.0, valinit=A, valstep=0.1)
    
    ax_freq = plt.axes([0.1, 0.05, 0.8, 0.05], facecolor='lightgrey')
    slider_freq = Slider(ax_freq, 'Frequency', 0.0005, 0.002, valinit=f, valstep=0.00005)
    
    def update(val):
        tol = slider_tol.val
        amp = slider_amp.val
        freq = slider_freq.val
        _, env_t = harmonic_envelope(t_values, sigma, amplitude=amp, frequency=freq)
        mask = np.abs(delta_t - env_t) < tol
        scatter_zeros.set_offsets(np.c_[t_values[mask], delta_t[mask]])
        line_env.set_ydata(env_t)
        # Update zero count display
        zero_count_text.set_text(f"Captured Zeros: {np.sum(mask)} / 99995")
        
        # Update histogram
        distances = np.abs(np.interp(zeta_zeros, t_values, delta_t) - np.interp(zeta_zeros, t_values, env_t))
        for rect, dist in zip(hist_bar, distances[:100]):
            rect.set_height(dist)
        fig.canvas.draw_idle()
    
    slider_tol.on_changed(update)
    slider_amp.on_changed(update)
    slider_freq.on_changed(update)
    
    # Set plot labels and title
    ax.set_title("Modular Drift and Harmonic Envelope (Interactive)")
    ax.set_xlabel("t")
    ax.set_ylabel("Modular Drift (radians)")
    ax.set_ylim(0, 2 * np.pi)
    ax.set_xlim(t_min, t_max)
    ax.legend()
    plt.show()


# Run the fully standalone interactive sieve plot
plot_interactive_sieve()
