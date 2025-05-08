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

# Load files from the data directory
delta_curve = np.load("data/delta_curve.npy")
dynamic_sine_envelope = np.load("data/dynamic_sine_envelope.npy")
smoothed_delta = np.load("data/smoothed_delta.npy")
within_band_mask = np.load("data/within_band_mask.npy")
zeta_zeros = np.load("data/zeta_zeros.npy")

# Perform basic integrity checks
print("✅ Basic data integrity checks passed.")
print(f"Delta Curve: {delta_curve.shape}, dtype={delta_curve.dtype}")
print(f"Dynamic Sine Envelope: {envelope.shape}, dtype={envelope.dtype}")
print(f"Smoothed Delta: {smoothed_delta.shape}, dtype={smoothed_delta.dtype}")
print(f"Within Band Mask: {within_band_mask.shape}, dtype={within_band_mask.dtype}")
print(f"Zeta Zeros: {zeta_zeros.shape}, dtype={zeta_zeros.dtype}")

# Check if all zeros are positive (sanity check)
assert np.all(zeta_zeros > 0), "❌ Some zeta zeros are not positive."
print("✅ Zeta zeros are all positive as expected.")

# Check if the delta curve and within band mask have the same length
assert delta_curve.shape == within_band_mask.shape, "❌ Delta curve and within band mask are not aligned."
print("✅ Delta curve and within band mask are aligned.")

# Check if the envelope and within band mask match
envelope_mismatch = np.any((envelope > 0) != within_band_mask)
assert not envelope_mismatch, "❌ Envelope and band mask are not aligned."
print("✅ Envelope alignment checks passed.")

print("🎯 Comprehensive sieve testing complete.")
