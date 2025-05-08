import os

def load_parameters(filepath):
    """
    Loads the sieve parameters from a text file.

    Parameters:
    - filepath (str): Path to the parameter file.

    Returns:
    - dict: Dictionary of parameters.
    """
    parameters = {}
    with open(filepath, "r") as file:
        for line in file:
            # Allow both "=" and ":" as separators
            if "=" in line:
                key, value = line.split("=", 1)
            elif ":" in line:
                key, value = line.split(":", 1)
            else:
                continue
            
            # Remove leading and trailing whitespace
            key = key.strip().replace(" ", "_")
            value = value.strip()
            
            # Convert the value to float if possible
            try:
                parameters[key] = float(value)
            except ValueError:
                print(f"Warning: Could not convert parameter '{key}' to float.")

    return parameters
    

def save_results(output_file, results):
    """
    Saves the sieve results to a text file.

    Parameters:
    - output_file (str): Path to the output file.
    - results (dict): Dictionary of results.
    """
    with open(output_file, "w") as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")


def log(message):
    """
    Simple logging function.

    Parameters:
    - message (str): The message to log.
    """
    print(f"[LOG] {message}")
