import numpy as np
import matplotlib.pyplot as plt

# Load the data files
delta_curve = np.load("delta_curve.npy")
dynamic_sine_envelope = np.load("dynamic_sine_envelope.npy")
smoothed_delta = np.load("smoothed_delta.npy")
within_band_mask = np.load("within_band_mask.npy")
zeta_zeros = np.load("zeta_zeros.npy")
known_zeros = np.load("zeta_zeros.npy")

print(f"Loaded {len(known_zeros)} known zeros.")

# Extract the sieve parameters from the text file
with open("sieve_parameters.txt", "r") as f:
    parameters = f.readlines()
    amplitude = float(parameters[0].split(":")[1].strip())
    frequency = float(parameters[1].split(":")[1].strip())
    smoothing_sigma = float(parameters[2].split(":")[1].strip())
    tolerance = float(parameters[3].split(":")[1].strip())

print(f"✅ Loaded Sieve Parameters:")
print(f"Amplitude: {amplitude}")
print(f"Frequency: {frequency}")
print(f"Smoothing Sigma: {smoothing_sigma}")
print(f"Tolerance: {tolerance}")

# Verify the within-band mask
detected_zeros = zeta_zeros[within_band_mask]
false_negatives = np.setdiff1d(known_zeros, detected_zeros)
false_positives = np.setdiff1d(detected_zeros, known_zeros)

print(f"\n🎯 Sieve Accuracy Results:")
print(f"True Positives: {len(detected_zeros)}")
print(f"False Negatives: {len(false_negatives)}")
print(f"False Positives: {len(false_positives)}")

# Plot the full envelope for sanity check
plt.figure(figsize=(12, 6))
plt.plot(dynamic_sine_envelope, color='blue', label='Dynamic Sine Envelope')
plt.title("Full Dynamic Sine Envelope - Verification")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()

# Plot the first 5000 points to verify seed region behavior
plt.figure(figsize=(12, 6))
plt.plot(dynamic_sine_envelope[:5000], color='green', label='Seed Region (First 5000 Samples)')
plt.title("Dynamic Sine Envelope - Seed Region")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
