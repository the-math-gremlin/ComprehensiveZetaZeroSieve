import numpy as np
import matplotlib.pyplot as plt

# Parameters from the paper
num_points = 100000
max_t = 100000  # Corresponds to the maximum t value in the dataset
t_values = np.linspace(1, max_t, num_points)

# Calculate the correct beat frequency
log_3 = np.log(3)
log_pi = np.log(np.pi)
frequency = abs(1/log_3 - 1/log_pi)

# Corrected amplitude scaling based on the paper
A0 = 0.15  # Peak amplitude from the paper, adjust if needed

# Regenerate the dynamic sine envelope
dynamic_sine_envelope = A0 * (1 - np.exp(-0.01 * t_values ** 0.5)) * np.sin(frequency * t_values)

# Save the corrected envelope
np.save("dynamic_sine_envelope.npy", dynamic_sine_envelope)

# Plot the full range for verification
plt.figure(figsize=(12, 6))
plt.plot(t_values, dynamic_sine_envelope, color='blue')
plt.title("Corrected Dynamic Sine Envelope - Full Range")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()

# Plot the seed region separately for detailed inspection
plt.figure(figsize=(12, 6))
plt.plot(t_values[:5000], dynamic_sine_envelope[:5000], color='green')
plt.title("Corrected Dynamic Sine Envelope - Seed Region (t < 5000)")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()
