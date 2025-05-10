import numpy as np

# Load known zeros and t-values
known_zeros = np.loadtxt("../data/zeta_zeros.txt")
t_values = np.loadtxt("../data/t_values.txt")

# Set parameters
AMPLITUDE = np.pi * np.abs(1 / np.log(3) - 1 / np.log(np.pi))
FREQUENCY = 1 / (2 * np.pi * np.log(3))
PHASE_SHIFT = 0  # Set to zero for now, adjust later if needed
TOLERANCE = 1e-10

# Calculate delta curve
delta_curve = np.abs(np.log(t_values / np.pi) - np.log(t_values / 3))
print(f"[DEBUG] Delta Curve Length: {len(delta_curve)}")
print(f"[DEBUG] Sample Delta Curve: {delta_curve[:10]}")

# Calculate sine envelope
envelope = AMPLITUDE * np.sin(2 * np.pi * FREQUENCY * np.log(t_values))
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
