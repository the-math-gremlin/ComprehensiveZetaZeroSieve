import numpy as np
import matplotlib.pyplot as plt

# Set the correct file path for the envelope
ENVELOPE_PATH = "data/dynamic_sine_envelope.npy"

# Define the parameters for the envelope regeneration
t_values = np.linspace(0, 100000, 100000)
base_amplitude = 0.08
decay_rate = 0.0008

# Regenerate the dynamic sine envelope
envelope = base_amplitude * np.exp(-decay_rate * t_values) * np.sin(t_values / 100)

# Save the regenerated envelope
np.save(ENVELOPE_PATH, envelope)
print(f"✅ Dynamic sine envelope regenerated and saved to {ENVELOPE_PATH}")

# Plot for verification
plt.figure(figsize=(12, 6))
plt.plot(t_values[:5000], envelope[:5000], color="green")
plt.title("Corrected Dynamic Sine Envelope - Seed Region (t < 5000)")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(t_values, envelope, color="blue")
plt.title("Corrected Dynamic Sine Envelope - Full Range")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()
