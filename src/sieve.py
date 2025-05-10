import numpy as np
import math
from math import exp, sqrt, pi

# Load known zeta zeros (first 100,000 imaginary parts) and reference delta
zeta_zeros = np.load("../data/zeta_zeros.npy")            # known nontrivial zeros
delta_ref  = np.load("../data/delta_curve.npy")           # reference raw drift Δ(t) from data

# Compute Riemann-Siegel theta approximately and accumulate phase difference
def theta_asymptotic(t):
    # Asymptotic Riemann-Siegel theta: θ(t) ≈ ½ t \ln(t/2π) - ½ t - π/8 
    return 0.5*t*math.log(t/(2*math.pi)) - 0.5*t - math.pi/8

delta_computed = []
cumulative_cycles = 0  # number of 2π cycles added (for unwrapping)
prev_phase = None
for n, t in enumerate(zeta_zeros, start=1):
    # Phase difference: θ(t_n) - nπ 
    phase_diff = theta_asymptotic(t) - n*math.pi
    # Unwrap: ensure phase_diff is within ±π of previous to avoid big jumps 
    if prev_phase is not None:
        # if jump > π, adjust by 2π cycles
        while phase_diff - prev_phase < -math.pi:
            phase_diff += 2*math.pi
            cumulative_cycles += 1
    prev_phase = phase_diff
    # Convert to degrees in [0, 360)
    delta_deg = (phase_diff % (2*math.pi)) * (180/math.pi)
    delta_computed.append(delta_deg)

delta_computed = np.array(delta_computed)
print("First 10 Δ(t) computed:", np.round(delta_computed[:10], 5))
print("First 10 Δ(t) reference:", np.round(delta_ref[:10], 5))

delta = delta_computed  # our Δ(t) from previous step
sigma = 5.0
# Construct Gaussian kernel (truncate at ±3σ for efficiency)
radius = int(3*sigma)
x = np.arange(-radius, radius+1)
gauss_kernel = np.exp(-0.5*(x/sigma)**2)
gauss_kernel /= gauss_kernel.sum()  # normalize

# Convolve Δ with Gaussian kernel
mu_computed = np.convolve(delta, gauss_kernel, mode='same')
mu_ref = np.load("../data/smoothed_delta.npy")
print("Max deviation between computed μ and reference μ:",
      np.max(np.abs(mu_computed - mu_ref)))

print("μ(t) first 10:", np.round(mu_computed[:10], 5))
print("Reference first 10:", np.round(mu_ref[:10], 5))

A = 12.2
f = 0.001
# Compute envelope E(t) for each zero index
envelope_computed = mu_computed + A * np.sin(f * np.log(zeta_zeros + 1))
envelope_ref = np.load("../data/dynamic_sine_envelope.npy")
print("Envelope difference (max):", np.max(np.abs(envelope_computed - envelope_ref)))

print("Envelope E(t) first 10:", np.round(envelope_computed[:10], 5))

epsilon = 0.875
within_band_mask = np.abs(delta - envelope_computed) <= epsilon
captured_count = np.sum(within_band_mask)
print("Captured zeros count:", captured_count)
print("Missed zeros count:", len(zeta_zeros) - captured_count)

missed_indices = np.where(~within_band_mask)[0]
missed_zeros = zeta_zeros[missed_indices]
print("Missed zero indices (0-based):", missed_indices)
print("Missed zero values:", np.round(missed_zeros, 8))

for idx in missed_indices:
    diff = delta[idx] - envelope_computed[idx]
    print(f"Index {idx+1} zero: Δ - E = {diff:.3f} (outside ±0.875)")
# Also check one captured example
idx = 3  # 4th zero (should be captured)
diff = delta[idx] - envelope_computed[idx]
print(f"Index {idx+1} zero: Δ - E = {diff:.3f} (within ±0.875)")

captured_zeros = zeta_zeros[within_band_mask]
print("Total captured zeros:", len(captured_zeros))
print("First 10 captured zeros:", np.round(captured_zeros[:10], 8))
print("Last 10 captured zeros:", np.round(captured_zeros[-10:], 8))

