import numpy as np
import os
import matplotlib.pyplot as plt
from utils import load_parameters, load_data_files

def precision_alignment_test(debug_mode=False):
    # Load parameters and data
    parameters = load_parameters()
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()

    # Calculate the smoothed centerline
    sigma = parameters["Smoothing_Sigma"]
    mu_t = np.convolve(delta_curve, np.ones(int(sigma)) / sigma, mode='same')

    # Reconstruct the dynamic sine envelope
    A = parameters["Amplitude"]
    f = parameters["Base_Frequency"]
    t_values = np.arange(1, len(delta_curve) + 1)
    envelope_reconstructed = mu_t + A * np.sin(2 * np.pi * f * np.log(t_values + 1))

    # Check alignment
    tolerance = parameters["Tolerance"]
    missed_zeros = []
    for zero in zeta_zeros:
        # Find the closest index to this zero
        index = int(np.round(zero))
        if index < len(envelope_reconstructed):
            delta_value = delta_curve[index]
            envelope_value = envelope_reconstructed[index]
            if abs(delta_value - envelope_value) > tolerance:
                missed_zeros.append((zero, delta_value, envelope_value))
                if debug_mode and len(missed_zeros) <= 10:
                    print(f"[DEBUG] Missed zero at t = {zero:.12f}, Delta = {delta_value:.6f}, Envelope = {envelope_value:.6f}")

    # Print summary
    print(f"[INFO] Precision alignment check completed.")
    print(f"[INFO] Total known zeros: {len(zeta_zeros)}")
    print(f"[INFO] Missed zeros: {len(missed_zeros)}")
    if missed_zeros:
        print(f"[INFO] First 10 missed zeros (if available):")
        for zero, delta, envelope in missed_zeros[:10]:
            print(f"t = {zero:.12f}, Delta = {delta:.6f}, Envelope = {envelope:.6f}")

    # Plot the centerline and envelope
    plt.figure(figsize=(15, 8))
    plt.plot(delta_curve, label='Delta Curve (Raw)', color='blue', linewidth=1)
    plt.plot(mu_t, label='Smoothed Centerline', color='green', linewidth=1)
    plt.plot(envelope_reconstructed, label='Reconstructed Envelope', color='red', linewidth=1)
    plt.scatter(zeta_zeros, [envelope_reconstructed[int(np.round(z))] for z in zeta_zeros], color='orange', s=8, label='Known Zeros')
    plt.title("Centerline and Envelope Precision Alignment")
    plt.xlabel("Index (t)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    precision_alignment_test(debug_mode=True)
