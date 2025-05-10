import numpy as np
import config

def load_data():
    delta_curve = np.load(config.DELTA_CURVE_FILE)
    dynamic_sine_envelope = np.load(config.DYNAMIC_SINE_ENVELOPE_FILE)
    within_band_mask = np.load(config.WITHIN_BAND_MASK_FILE)
    return delta_curve, dynamic_sine_envelope, within_band_mask

def run_basic_sieve(delta_curve, dynamic_sine_envelope, within_band_mask, verbose=False):
    detected_zeros = []
    for i in range(len(delta_curve)):
        if within_band_mask[i] == 1 and delta_curve[i] <= dynamic_sine_envelope[i]:
            detected_zeros.append(i)
            if verbose:
                print(f"[ZERO] Index: {i}, Delta: {delta_curve[i]}, Envelope: {dynamic_sine_envelope[i]}")
    return detected_zeros
