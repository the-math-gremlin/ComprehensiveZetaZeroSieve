# Data Directory

This directory contains the core data files for the Comprehensive Zeta Zero Sieve.

## File Descriptions

- **delta_curve.npy** - The precomputed delta curve used in the sieve algorithm.
- **dynamic_sine_envelope.npy** - The dynamic sine envelope that defines the allowed zero band.
- **sieve_parameters.txt** - The core parameters for the sieve (e.g., amplitude, frequency, sigma, tolerance).
- **smoothed_delta.npy** - The smoothed version of the delta curve used for enhanced precision.
- **within_band_mask.npy** - The binary mask indicating which points fall within the allowed zero band.
- **zeta_zeros.npy** - The known nontrivial zeros of the Riemann zeta function used for validation.
