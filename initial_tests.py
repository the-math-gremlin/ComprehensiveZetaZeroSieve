import numpy as np
import os

# Paths to the data files
DATA_DIR = './data/'
delta_curve_file = os.path.join(DATA_DIR, 'delta_curve.npy')
dynamic_sine_file = os.path.join(DATA_DIR, 'dynamic_sine_envelope.npy')
smoothed_delta_file = os.path.join(DATA_DIR, 'smoothed_delta.npy')
within_band_mask_file = os.path.join(DATA_DIR, 'within_band_mask.npy')
zeta_zeros_file = os.path.join(DATA_DIR, 'zeta_zeros.npy')

# Load the data files
try:
    delta_curve = np.load(delta_curve_file)
    dynamic_sine_envelope = np.load(dynamic_sine_file)
    smoothed_delta = np.load(smoothed_delta_file)
    within_band_mask = np.load(within_band_mask_file)
    zeta_zeros = np.load(zeta_zeros_file)
    print("✅ All data files loaded successfully.")
except Exception as e:
    print(f"❌ Error loading data files: {e}")

# Check basic properties
print(f"Delta Curve: {delta_curve.shape}, dtype={delta_curve.dtype}")
print(f"Dynamic Sine Envelope: {dynamic_sine_envelope.shape}, dtype={dynamic_sine_envelope.dtype}")
print(f"Smoothed Delta: {smoothed_delta.shape}, dtype={smoothed_delta.dtype}")
print(f"Within Band Mask: {within_band_mask.shape}, dtype={within_band_mask.dtype}")
print(f"Zeta Zeros: {zeta_zeros.shape}, dtype={zeta_zeros.dtype}")

# Quick sanity check on the zeros
if np.all(zeta_zeros > 0):
    print("✅ Zeta zeros are all positive as expected.")
else:
    print("❌ Some zeta zeros have unexpected negative values.")

# Check for alignment between the mask and delta curve
if delta_curve.shape == within_band_mask.shape:
    print("✅ Delta curve and within band mask are aligned.")
else:
    print("❌ Mismatch between delta curve and within band mask dimensions.")

print("Initial data verification complete.")
