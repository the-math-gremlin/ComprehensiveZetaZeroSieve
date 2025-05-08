import numpy as np
import time

# Load data files
delta_curve = np.load("data/delta_curve.npy")
dynamic_sine_envelope = np.load("data/dynamic_sine_envelope.npy")
smoothed_delta = np.load("data/smoothed_delta.npy")
within_band_mask = np.load("data/within_band_mask.npy")
zeta_zeros = np.load("data/zeta_zeros.npy")

# Basic integrity checks
assert delta_curve.shape == (100000,), "Delta curve shape mismatch"
assert dynamic_sine_envelope.shape == (100000,), "Sine envelope shape mismatch"
assert smoothed_delta.shape == (100000,), "Smoothed delta shape mismatch"
assert within_band_mask.shape == (100000,), "Within band mask shape mismatch"
assert zeta_zeros.shape == (100000,), "Zeta zeros shape mismatch"
print("✅ Basic data integrity checks passed.")

# Check for valid data ranges
assert np.all(zeta_zeros > 0), "❌ Zeta zeros must be positive"
assert np.all(delta_curve > 0), "❌ Delta curve must be positive"
assert np.all(smoothed_delta > 0), "❌ Smoothed delta must be positive"
print("✅ Data range checks passed.")

# Check for envelope alignment
tolerance = 1e-12  # Adjust as needed
envelope_mismatch = np.any((delta_curve > (dynamic_sine_envelope + tolerance)) != within_band_mask)
assert not envelope_mismatch, "❌ Envelope and band mask are not aligned"
print("✅ Envelope alignment checks passed.")

# Sieve accuracy check
print("\n🔄 Running sieve accuracy check...")
start_time = time.time()
detected_zeros = zeta_zeros[within_band_mask]
expected_zeros = zeta_zeros

# Check that the sieve captures all known zeros
false_negatives = np.setdiff1d(expected_zeros, detected_zeros)
false_positives = np.setdiff1d(detected_zeros, expected_zeros)

if len(false_negatives) == 0 and len(false_positives) == 0:
    print("✅ Sieve correctly identified all known zeros.")
else:
    print(f"❌ Sieve failed with {len(false_negatives)} false negatives and {len(false_positives)} false positives.")
    print(f"⚠️ False Negatives: {false_negatives[:10]}")
    print(f"⚠️ False Positives: {false_positives[:10]}")

print(f"🕒 Sieve accuracy check completed in {time.time() - start_time:.4f} seconds.")

# Boundary testing
print("\n🔎 Running boundary tests...")
try:
    # Test zero boundaries
    assert delta_curve[0] > 0, "❌ Delta curve must be positive at boundary"
    assert delta_curve[-1] > 0, "❌ Delta curve must be positive at boundary"
    assert dynamic_sine_envelope[0] > 0, "❌ Sine envelope must be positive at boundary"
    assert dynamic_sine_envelope[-1] > 0, "❌ Sine envelope must be positive at boundary"
    print("✅ Boundary checks passed.")
except AssertionError as e:
    print(str(e))

print("\n🎯 Comprehensive sieve testing complete.")
