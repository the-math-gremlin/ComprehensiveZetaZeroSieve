import numpy as np
import matplotlib.pyplot as plt
import os

# Load the required data files
data_dir = os.path.abspath('../data')
delta_curve = np.load(os.path.join(data_dir, 'delta_curve.npy'))
dynamic_sine_envelope = np.load(os.path.join(data_dir, 'dynamic_sine_envelope.npy'))
within_band_mask = np.load(os.path.join(data_dir, 'within_band_mask.npy'))
zeta_zeros = np.load(os.path.join(data_dir, 'zeta_zeros.npy'))

# Plot the delta curve, sine envelope, and known zeros
plt.figure(figsize=(15, 8))
plt.plot(delta_curve, label='Delta Curve (Raw)', color='blue', linewidth=1)
plt.plot(dynamic_sine_envelope, label='Reconstructed Envelope', color='red', linewidth=1)

# Overlay the within-band mask
within_band_indices = np.where(within_band_mask == 1)[0]
plt.scatter(within_band_indices, dynamic_sine_envelope[within_band_indices], color='green', s=1, label='Within-Band Mask')

# Overlay known zeros
plt.scatter(zeta_zeros, dynamic_sine_envelope[(zeta_zeros - 1).astype(int)], color='orange', s=8, label='Known Zeros')

# Highlight missed zeros if any
missed_zeros_file = os.path.join(data_dir, 'missed_zeros.npy')
if os.path.exists(missed_zeros_file):
    missed_zeros = np.load(missed_zeros_file)
    plt.scatter(missed_zeros, dynamic_sine_envelope[(missed_zeros - 1).astype(int)], color='purple', s=20, label='Missed Zeros')
    print(f"[INFO] Highlighting {len(missed_zeros)} missed zeros: {missed_zeros[:10]}")
else:
    print("[INFO] No missed zeros file found. Skipping missed zero overlay.")

# Add labels and legend
plt.title('Reconstructed Envelope vs Delta Curve')
plt.xlabel('Index (t)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
