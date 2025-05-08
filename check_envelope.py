import numpy as np
import matplotlib.pyplot as plt

# Load the dynamic sine envelope
envelope = np.load("data/dynamic_sine_envelope.npy")

# Plot the full envelope to verify its shape
plt.plot(envelope, color='blue')
plt.title("Loaded Dynamic Sine Envelope")
plt.xlabel("Index (t)")
plt.ylabel("Amplitude")
plt.show()
