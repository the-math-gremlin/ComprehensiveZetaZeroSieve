import numpy as np
from utils import load_data_files

def early_zero_diagnostics(limit=20):
    # Load all necessary data files
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    
    # Prepare the diagnostic output
    print("\n=== Early Zero Diagnostics ===")
    print("{:<8} | {:<15} | {:<15} | {:<15} | {:<15}".format("Index", "t_value", "Delta Curve", "Envelope", "Known Zero"))
    print("-" * 70)
    
    for idx in range(min(limit, len(zeta_zeros))):
        t_value = zeta_zeros[idx]
        delta_val = delta_curve[idx]
        envelope_val = dynamic_sine_envelope[idx]
        
        # Check if this is a known zero (within tolerance)
        is_known_zero = np.isclose(delta_val, envelope_val, rtol=1e-12, atol=1e-12)
        
        # Print the diagnostics for this zero
        print("{:<8} | {:<15.6f} | {:<15.6f} | {:<15.6f} | {}".format(
            idx, t_value, delta_val, envelope_val, "Yes" if is_known_zero else "No"
        ))
    
    print("\nDiagnostic check complete.\n")

if __name__ == "__main__":
    early_zero_diagnostics(limit=20)
