import numpy as np

# Load the current delta curve and dynamic sine envelope
delta_curve = np.load("data/delta_curve.npy")
dynamic_sine_envelope = np.load("data/dynamic_sine_envelope.npy")

# Generate a new within-band mask
within_band_mask = delta_curve > dynamic_sine_envelope

# Save the new mask
np.save("data/within_band_mask.npy", within_band_mask)

print("✅ Successfully regenerated within_band_mask.npy")
