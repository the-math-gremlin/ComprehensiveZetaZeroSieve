import numpy as np
from scipy.ndimage import gaussian_filter1d
from utils import log

def run_sieve(delta_curve, envelope, within_band_mask, known_zeros, params, limit=100000):
    # Extract parameters
    A = params["Amplitude"]
    f = params["Base_Frequency"]
    sigma = params["Smoothing_Sigma"]
    tolerance_radius = int(np.ceil(params["Tolerance"] * 10))
    seed_region_end = params["Seed_Region_End"]
    phi = params["Phase_Shift"]

    # Smooth the delta curve to get the centerline (mu_t)
    mu_t = gaussian_filter1d(delta_curve, sigma)

    # Calculate the expected envelope
    t_values = np.arange(1, len(delta_curve) + 1)
    envelope_reconstructed = mu_t + A * np.sin(2 * np.pi * f * np.log(t_values + 1) + phi)

    # Convert known zeros to indices
    known_zero_indices = set(int(round(zero)) for zero in known_zeros)

    # Exclude the seed region
    known_zero_indices = {z for z in known_zero_indices if z > seed_region_end}

    true_positives = 0
    false_negatives = 0
    false_positives = 0

    for i in range(min(len(within_band_mask), limit)):
        if within_band_mask[i]:
            # Check if this index is a known zero
            if i in known_zero_indices:
                true_positives += 1
            else:
                false_positives += 1

        # Optional verbose logging for progress
        if i > 0 and i % 10000 == 0:
            log(f"Checked index {i} / {limit}")

    # Count remaining known zeros as false negatives
    false_negatives = len(known_zero_indices - set(range(limit)))

    return true_positives, false_negatives, false_positives
