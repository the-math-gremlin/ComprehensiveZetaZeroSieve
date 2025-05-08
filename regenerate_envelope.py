import numpy as np
import matplotlib.pyplot as plt

# Envelope parameters from the paper
A = 0.15  # Typical amplitude in the paper's range (0.1 to 0.2)
f = abs(1 / np.log(3) - 1 / np.log(np.pi))  # Beat frequency from paper
tolerance = 0.875
seed_region_length = 50

# Generate the full envelope
t = np.arange(1, 100001)
mu_t = np.log(t)  # Centerline approximation
envelope = A * np.sin(f * mu_t)

# Apply the seed region adjustment
seed_scale = np.linspace(0.01, A, seed_region_length)
envelope[:seed_region_length] = seed_scale * np.sin(f * mu_t[:seed_region_length])

# Save the regenerated envelope
np.save("data/dynamic_sine_envelope.npy", envelope)

# Plot the new envelope to verify
plt.figure(figsize=(14, 8))
plt.plot(envelope, color='dodgerblue', linewidth=1.2)
plt.title("Regenerated Dynamic Sine Envelope - Full Range")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 8))
plt.plot(envelope[:500], color='orange', linewidth=1.2)
plt.title("Regenerated Dynamic Sine Envelope - Seed Region (First 500 Samples)")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

print("✅ Successfully regenerated dynamic_sine_envelope.npy")
