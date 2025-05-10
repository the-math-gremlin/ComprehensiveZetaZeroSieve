import numpy as np
from utils import load_data_files, calculate_phase

def early_zero_diagnostics(limit=20, phase_tolerance=1e-12):
    # Load all necessary data files
    delta_curve, dynamic_sine_envelope, within_band_mask, zeta_zeros = load_data_files()
    
    # Calculate the phase alignment
    phase_curve = calculate_phase(delta_curve)
    phase_envelope = calculate_phase(dynamic_sine_envelope)
    
    # Prepare the diagnostic output
    print("\n=== Early Zero Diagnostics with Phase Alignment ===")
    print("{:<8} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15}".format(
        "Index", "t_value", "Delta Curve", "Envelope", "Phase Match", "Known Zero"
    ))
    print("-" * 100)
    
    for idx in range(min(limit, len(zeta_zeros))):
        t_value = zeta_zeros[idx]
        delta_val = delta_curve[idx]
        envelope_val = dynamic_sine_envelope[idx]
        phase_delta = phase_curve[idx]
        phase_envelope_val = phase_envelope[idx]
        
        # Check for envelope match
        is_known_zero = np.isclose(delta_val, envelope_val, rtol=1e-12, atol=1e-12)
        
        # Check for phase match
        phase_match = np.isclose(phase_delta, phase_envelope_val, rtol=1e-12, atol=phase_tolerance)
        
        # Print the diagnostics for this zero
        print("{:<8} | {:<15.6f} | {:<15.6f} | {:<15.6f} | {:<15} | {}".format(
            idx, t_value, delta_val, envelope_val, "Yes" if phase_match else "No", "Yes" if is_known_zero else "No"
        ))
    
    print("\nDiagnostic check complete.\n")

if __name__ == "__main__":
    early_zero_diagnostics(limit=20)
