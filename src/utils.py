from scipy.ndimage import gaussian_filter1d

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
