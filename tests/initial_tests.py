import numpy as np
import os

# Set the data directory
DATA_DIR = "data"

# Define the paths to the required files
delta_curve_path = os.path.join(DATA_DIR, "delta_curve.npy")
envelope_path = os.path.join(DATA_DIR, "dynamic_sine_envelope.npy")
smoothed_delta_path = os.path.join(DATA_DIR, "smoothed_delta.npy")
within_band_mask_path = os.path.join(DATA_DIR, "within_band_mask.npy")
zeta_zeros_path = os.path.join(DATA_DIR, "zeta_zeros.npy")

# Load the data files
delta_curve = np.load(delta_curve_path)
envelope = np.load(envelope_path)
smoothed_delta = np.load(smoothed_delta_path)
within_band_mask = np.load(within_band_mask_path)
zeta_zeros = np.load(zeta_zeros_path)

print("✅ All data files loaded successfully.")
print(f"Delta Curve: {delta_curve.shape}, dtype={delta_curve.dtype}")
print(f"Dynamic Sine Envelope: {envelope.shape}, dtype={envelope.dtype}")
print(f"Smoothed Delta: {smoothed_delta.shape}, dtype={smoothed_delta.dtype}")
print(f"Within Band Mask: {within_band_mask.shape}, dtype={within_band_mask.dtype}")
print(f"Zeta Zeros: {zeta_zeros.shape}, dtype={zeta_zeros.dtype}")

# Verify that all zeta zeros are positive
assert np.all(zeta_zeros > 0), "❌ Some zeta zeros are not positive."
print("✅ Zeta zeros are all positive as expected.")

# Verify that the delta curve and within band mask are aligned
assert delta_curve.shape == within_band_mask.shape, "❌ Delta curve and within band mask are not aligned."
print("✅ Delta curve and within band mask are aligned.")

print("🎯 Initial data verification complete.")
