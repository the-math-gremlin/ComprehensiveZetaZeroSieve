import numpy as np
from utils import calculate_modular_drift, calculate_envelope
import config
import os

def main():
    # Load t values
    t_values = np.arange(1, 100001, dtype=np.float64)

    # Calculate the modular drift
    delta_curve = calculate_modular_drift(t_values)

    # Calculate the envelope
    amplitude = config.AMPLITUDE
    frequency = config.FREQUENCY
    phase_shift = config.PHASE_SHIFT
    smoothing_sigma = config.SMOOTHING_SIGMA

    envelope, mu_t = calculate_envelope(delta_curve, t_values, amplitude, frequency, phase_shift, smoothing_sigma)

    # Save the outputs for verification
    np.save("../data/delta_curve.npy", delta_curve)
    np.save("../data/dynamic_sine_envelope.npy", envelope)
    np.save("../data/centerline.npy", mu_t)

    print("[INFO] Drift and envelope calculated successfully.")

if __name__ == "__main__":
    main()
