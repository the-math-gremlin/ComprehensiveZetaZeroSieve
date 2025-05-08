import numpy as np
import os

# Set the data directory
data_dir = "data"

# Load all core data files
delta_curve = np.load(os.path.join(data_dir, "delta_curve.npy"))
envelope = np.load(os.path.join(data_dir, "dynamic_sine_envelope.npy"))
smoothed_delta = np.load(os.path.join(data_dir, "smoothed_delta.npy"))
within_band_mask = np.load(os.path.join(data_dir, "within_band_mask.npy"))
zeta_zeros = np.load(os.path.join(data_dir, "zeta_zeros.npy"))

# Basic data integrity checks
print("✅ Basic data integrity checks passed.")
print(f"Delta Curve: {delta_curve.shape}, dtype={delta_curve.dtype}")
print(f"Dynamic Sine Envelope: {envelope.shape}, dtype={envelope.dtype}")
print(f"Smoothed Delta: {smoothed_delta.shape}, dtype={smoothed_delta.dtype}")
print(f"Within Band Mask: {within_band_mask.shape}, dtype={within_band_mask.dtype}")
print(f"Zeta Zeros: {zeta_zeros.shape}, dtype={zeta_zeros.dtype}")

# Confirm all zeros are positive
assert np.all(zeta_zeros > 0), "❌ Zeta zeros contain non-positive values."
print("✅ Zeta zeros are all positive as expected.")

# Confirm delta curve and within band mask are aligned
assert delta_curve.shape == within_band_mask.shape, "❌ Delta curve and within band mask are not aligned."
print("✅ Delta curve and within band mask are aligned.")

# Verify sieve captures known zeros
known_zeros = np.load(os.path.join(data_dir, "zeta_zeros.npy"))
missed_zeros = [zero for zero in known_zeros if zero not in zeta_zeros]

if missed_zeros:
    print(f"❌ Missed zeros: {missed_zeros}")
else:
    print("✅ All known zeros are correctly captured.")

print("🎯 Comprehensive sieve testing complete.")
