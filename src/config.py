import os

def load_parameters(parameter_file="data/sieve_parameters.txt"):
    parameters = {}
    try:
        with open(parameter_file, "r") as file:
            for line in file:
                if ":" in line:
                    key, value = line.strip().split(":")
                    parameters[key.strip()] = float(value.strip())
        return parameters
    except Exception as e:
        print(f"Error loading parameters: {e}")
        return None
