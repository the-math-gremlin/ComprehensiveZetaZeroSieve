import numpy as np

# Load known zeros and t-values
known_zeros = np.load("../data/zeta_zeros.npy")
t_values = np.load("../data/t_values.npy")

# Set parameters
AMPLITUDE = np.pi * np.abs(1 / np.log(3) - 1 / np.log(np.pi))
FREQUENCY = np.abs(1 / np.log(3) - 1 / np.log(np.pi))
PHASE_SHIFT = 0  # Set to zero for now, adjust later if needed
TOLERANCE = 0.875

# Calculate delta curve
theta_3 = 2 * np.pi * (np.log(t_values) / np.log(3) % 1)
theta_pi = 2 * np.pi * (np.log(t_values) / np.log(np.pi) % 1)
delta_curve = np.minimum(np.abs(theta_3 - theta_pi), 2 * np.pi - np.abs(theta_3 - theta_pi))

print(f"[DEBUG] Delta Curve Length: {len(delta_curve)}")
print(f"[DEBUG] Sample Delta Curve: {delta_curve[:10]}")

# Calculate sine envelope
mu_t = np.mean(delta_curve)  # Use a rough average for now, refine later
envelope = mu_t + AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * np.log(t_values) + PHASE_SHIFT)

print(f"[DEBUG] Envelope Length: {len(envelope)}")
print(f"[DEBUG] Sample Envelope: {envelope[:10]}")

# Identify zeros
potential_zeros = []
for i, (delta, env) in enumerate(zip(delta_curve, envelope)):
    if abs(delta - env) < TOLERANCE:
        potential_zeros.append(t_values[i])

print(f"[INFO] Detected {len(potential_zeros)} potential zeros.")

# Verify zeros
true_positives = sum(1 for zero in potential_zeros if zero in known_zeros)
false_positives = len(potential_zeros) - true_positives
missed_zeros = len(known_zeros) - true_positives

print("\n=== Zero Verification Summary ===")
print(f"Total Detected Zeros: {len(potential_zeros)}")
print(f"Total Known Zeros: {len(known_zeros)}")
print(f"True Positives: {true_positives}")
print(f"False Positives: {false_positives}")
print(f"Missed Zeros: {missed_zeros}")
