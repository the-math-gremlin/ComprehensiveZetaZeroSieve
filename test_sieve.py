import numpy as np
import matplotlib.pyplot as plt

# Parameters from your paper (approximate, can be adjusted if needed)
SEED_REGION_LIMIT = 5000
FULL_RANGE = 100000
AMPLITUDE_SCALE = 0.15  # Adjust this if the envelope seems too flat or too steep
FREQUENCY_SCALE = 0.01
DECAY_RATE = 0.005  # Controls how quickly the oscillations decay

# Generate the corrected dynamic sine envelope
t_values = np.arange(FULL_RANGE)
envelope = np.zeros(FULL_RANGE)

# Generate the seed region
for t in range(SEED_REGION_LIMIT):
    envelope[t] = AMPLITUDE_SCALE * np.sin(FREQUENCY_SCALE * t) * np.exp(-DECAY_RATE * t)

# Extend the envelope smoothly into the full range
max_seed_amplitude = np.max(np.abs(envelope[:SEED_REGION_LIMIT]))
for t in range(SEED_REGION_LIMIT, FULL_RANGE):
    # Gradually increase the amplitude to stabilize near the maximum seed amplitude
    envelope[t] = max_seed_amplitude * (1 - np.exp(-DECAY_RATE * (t - SEED_REGION_LIMIT)))

# Save the corrected envelope to file
output_path = 'data/dynamic_sine_envelope.npy'
np.save(output_path, envelope)
print(f"Corrected dynamic sine envelope saved to {output_path}")

# Plot the corrected envelope
plt.figure(figsize=(10, 6))
plt.plot(envelope, color='blue')
plt.title("Corrected Dynamic Sine Envelope - Full Range")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(envelope[:SEED_REGION_LIMIT], color='green')
plt.title("Corrected Dynamic Sine Envelope - Seed Region (t < 5000)")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()
