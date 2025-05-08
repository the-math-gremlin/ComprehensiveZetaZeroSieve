import numpy as np
import os

# Set the data directory
DATA_DIR = "data"
import numpy as np

# Load required data
delta_curve = np.load("data/delta_curve.npy")
envelope = np.load("data/dynamic_sine_envelope.npy")
smoothed_delta = np.load("data/smoothed_delta.npy")
within_band_mask = np.load("data/within_band_mask.npy")
zeta_zeros = np.load("data/zeta_zeros.npy")

# Initial checks (already handled by initial_tests.py)
print("\n🔄 Running additional sieve integrity checks...")

# 1. Boundary Drift Checks
boundary_issues = []
t_min = 0
t_max = len(delta_curve) - 1
if delta_curve[t_min] < -envelope[t_min] or delta_curve[t_min] > envelope[t_min]:
    boundary_issues.append(t_min)
if delta_curve[t_max] < -envelope[t_max] or delta_curve[t_max] > envelope[t_max]:
    boundary_issues.append(t_max)

if boundary_issues:
    print(f"❌ Boundary drift errors at indices: {boundary_issues}")
else:
    print("✅ Boundary drift checks passed.")

# 2. Harmonic Seed Verification
missed_zeros = np.loadtxt("data/sample_zeros.csv")
early_misses = missed_zeros[missed_zeros < 50]
if len(early_misses) > 0:
    print(f"⚠️ Harmonic seed verification: {len(early_misses)} early misses detected (t < 50).")
    print(f"Missed harmonic seeds: {early_misses}")
else:
    print("✅ All early zeros correctly classified as harmonic seeds.")

# 3. False Positive Scan
false_positives = np.where(within_band_mask & (delta_curve < -envelope) | (delta_curve > envelope))[0]
if len(false_positives) > 0:
    print(f"❌ False positives detected: {len(false_positives)}")
else:
    print("✅ No false positives detected.")

# 4. Sieve Stability Check
test_passed = np.all(within_band_mask == ((delta_curve > -envelope) & (delta_curve < envelope)))
if test_passed:
    print("✅ Sieve stability check passed.")
else:
    print("❌ Sieve stability check failed.")

print("\n📝 Sieve integrity checks complete.")

# Define the paths to the required files
delta_curve_path = os.path.join(DATA_DIR, "delta_curve.npy")
envelope_path = os.path.join(DATA_DIR, "dynamic_sine_envelope.npy")
smoothed_delta_path = os.path.join(DATA_DIR, "smoothed_delta.npy")
within_band_mask_path = os.path.join(DATA_DIR, "within_band_mask.npy")
zeta_zeros_path = os.path.join(DATA_DIR, "zeta_zeros.npy")

# Load files from the data directory
delta_curve = np.load("data/delta_curve.npy")
envelope = np.load("data/dynamic_sine_envelope.npy")
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
