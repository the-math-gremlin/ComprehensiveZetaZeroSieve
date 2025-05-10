import numpy as np
import os

# Load the required data files
data_dir = os.path.abspath('../data')
delta_curve = np.load(os.path.join(data_dir, 'delta_curve.npy'))
dynamic_sine_envelope = np.load(os.path.join(data_dir, 'dynamic_sine_envelope.npy'))
zeta_zeros = np.load(os.path.join(data_dir, 'zeta_zeros.npy'))

# Set the number of initial points to inspect
inspection_count = 20

print("\n=== Early Zero Diagnostics ===")
print(f"{'Index':>6} | {'t_value':>12} | {'Delta Curve':>15} | {'Envelope':>15} | {'Known Zero':>12}")
print("-" * 70)

for idx in range(inspection_count):
    t_value = zeta_zeros[idx]
    delta_value = delta_curve[idx]
    envelope_value = dynamic_sine_envelope[idx]
    
    # Check if this index corresponds to a known zero
    is_zero = t_value in zeta_zeros
    
    print(f"{idx:>6} | {t_value:>12.6f} | {delta_value:>15.6f} | {envelope_value:>15.6f} | {'Yes' if is_zero else 'No':>12}")

print("\nDiagnostic check complete.\n")
