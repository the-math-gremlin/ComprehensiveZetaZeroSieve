import numpy as np
import subprocess
import os
from itertools import product

# Define the ranges for the parameters you want to sweep
tolerance_range = np.linspace(0.8, 1.0, 5)
amplitude_range = np.linspace(11.0, 13.0, 5)
frequency_range = np.linspace(0.0008, 0.0012, 5)

# Create a directory to store the results
results_dir = "../results"
os.makedirs(results_dir, exist_ok=True)

# Create a log file to store the results
log_file = os.path.join(results_dir, "parameter_sweep_results.txt")
with open(log_file, "w") as f:
    f.write("Tolerance,Amplitude,Frequency,True Positives,False Positives,Missed Zeros\n")

# Run the sweep
for tolerance, amplitude, frequency in product(tolerance_range, amplitude_range, frequency_range):
    # Update the parameters file
    params_file = "../data/sieve_parameters.txt"
    with open(params_file, "w") as f:
        f.write(f"Amplitude={amplitude}\n")
        f.write(f"Frequency={frequency}\n")
        f.write(f"Tolerance={tolerance}\n")
    
    # Run the diagnostics test
    result = subprocess.run(
        ["python", "sieve_diagnostics_test.py", "debug_mode=True", "--limit=10000"],
        capture_output=True,
        text=True
    )
    
    # Parse the output for true positives, false positives, and missed zeros
    output_lines = result.stdout.split("\n")
    true_positives = next((line.split(":")[1].strip() for line in output_lines if "True Positives:" in line), "N/A")
    false_positives = next((line.split(":")[1].strip() for line in output_lines if "False Positives:" in line), "N/A")
    missed_zeros = next((line.split(":")[1].strip() for line in output_lines if "Missed Zeros:" in line), "N/A")
    
    # Save the results
    with open(log_file, "a") as f:
        f.write(f"{tolerance},{amplitude},{frequency},{true_positives},{false_positives},{missed_zeros}\n")
    
    print(f"Tested Tolerance={tolerance}, Amplitude={amplitude}, Frequency={frequency}")

# Analyze the results to find the best parameter set
best_set = None
best_score = float('-inf')
best_line = None

with open(log_file, "r") as f:
    next(f)  # Skip header
    for line in f:
        tol, amp, freq, tp, fp, mz = line.strip().split(",")
        if tp != "N/A" and fp != "N/A" and mz != "N/A":
            tp, fp, mz = int(tp), int(fp), int(mz)
            # Score is true positives minus false positives (penalize missed zeros heavily)
            score = tp - (fp * 2) - (mz * 10)

            if score > best_score:
                best_score = score
                best_set = (tol, amp, freq, tp, fp, mz)
                best_line = line.strip()

# Print the best parameter set
if best_set is not None:
    print("\n[INFO] Best Parameter Set:")
    print(f"Tolerance: {best_set[0]}")
    print(f"Amplitude: {best_set[1]}")
    print(f"Frequency: {best_set[2]}")
    print(f"True Positives: {best_set[3]}")
    print(f"False Positives: {best_set[4]}")
    print(f"Missed Zeros: {best_set[5]}")

    # Save the best set for easy reference
    best_file = os.path.join(results_dir, "best_parameters.txt")
    with open(best_file, "w") as f:
        f.write(best_line + "\n")

    print(f"[INFO] Best parameters saved to {best_file}")
else:
    print("[WARNING] No valid parameter sets found.")

print("[INFO] Parameter sweep complete. Results saved to", log_file)
