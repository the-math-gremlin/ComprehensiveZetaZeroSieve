import numpy as np
import config
from utils import calculate_modular_drift, calculate_dynamic_envelope, run_sieve

def main():
    # Generate dynamic t-values for the critical line
    t_values = np.linspace(config.MIN_T, config.MAX_T, config.NUM_POINTS)

    # Calculate the modular drift and dynamic envelope functions
    delta_curve = calculate_modular_drift(t_values)
    envelope = calculate_dynamic_envelope(t_values)

    # Print debug information
    print("\n=== Debug Information ===")
    print(f"Sample Delta Curve: {delta_curve[:10]}")
    print(f"Sample Envelope: {envelope[:10]}")
    print(f"Max Envelope Value: {np.max(envelope)}")
    print(f"Min Envelope Value: {np.min(envelope)}")
    print(f"\nAmplitude: {config.AMPLITUDE}")

    # Run the sieve
    detected_zeros = run_sieve(t_values, delta_curve, envelope, config.TOLERANCE)

    # Print results
    print("\n=== Sieve Results ===")
    print(f"Detected {len(detected_zeros)} potential zeros")
    for zero in detected_zeros[:20]:  # Print the first 20 for sanity check
        print(f"t = {zero:.10f}")

    print("\nSieve complete.")

if __name__ == "__main__":
    main()
