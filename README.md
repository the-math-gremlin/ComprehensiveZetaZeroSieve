# Comprehensive Zeta Zero Sieve

This script implements the comprehensive zeta zero sieve described in the paper "Phase-Locked Modular Resonance and the Structure of Zeta Zeros" by Sadie A. Sherratt. The sieve identifies candidate nontrivial zeta zeros using a combination of modular drift, harmonic envelope construction, and symbolic resonance. The approach is purely geometric, relying on the modular alignment of logarithmic spirals in bases 3 and π.

## Features
- High-speed harmonic zero identification
- Configurable parameters for precision tuning
- Detailed diagnostic logging
- Real-time progress updates
- Automatic missed zero detection

## Installation
Ensure you have the required packages:
```
pip install numpy
```

Clone the repository and navigate to the source directory:
```
git clone https://github.com/the-math-gremlin/ComprehensiveZetaZeroSieve.git
cd ComprehensiveZetaZeroSieve/src
```

## Running the Sieve
Run the sieve with default parameters:
```
python main.py --verbose
```

Limit the number of indices for a faster test:
```
python main.py --limit 10000 --verbose
```

## Configuration
The sieve parameters can be adjusted in the `sieve_parameters.txt` file:
- `Amplitude`: Maximum envelope height (default: 12.2)
- `Base_Frequency`: Harmonic base frequency (default: 0.03667)
- `Smoothing_Sigma`: Width of the centerline smoothing kernel (default: 5.0)
- `Tolerance`: Maximum angular deviation for zero identification (default: 0.875)
- `Seed_Region_End`: Number of initial indices to exclude (default: 50)

## Output
The sieve produces a detailed diagnostic log (`sieve_diagnostics.log`) containing:
- True Positives: Correctly identified zeros
- False Positives: Non-zero points incorrectly classified as zeros
- False Negatives: Missed zeros
- Known Missed Zeros: The specific set of zeros that are always missed (typically 5)

## Known Limitations
- Five of the first few zeros (within the seed region) are always missed
- Requires precomputed data files for delta curve and envelope

## License
This project is open-source and licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Special thanks to the open mathematical community for inspiration and support. This project was developed collaboratively with the assistance of ChatGPT-4o, OpenAI.

## Contact
For questions, feedback, or collaboration opportunities, please reach out to the author at sadie@sherrattmath.org.

