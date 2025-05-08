import os

def load_parameters(filepath):
    """
    Loads the sieve parameters from a text file.
    Falls back to default parameters if the file is missing or corrupted.

    Parameters:
    - filepath (str): Path to the parameter file.

    Returns:
    - dict: Dictionary of parameters.
    """
    parameters = {}
    try:
        with open(filepath, "r") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip().replace(" ", "_")
                    value = value.strip()
                    parameters[key] = float(value)
    except FileNotFoundError:
        print(f"[Warning] Parameter file not found at '{filepath}'. Using default parameters.")
    except ValueError as e:
        print(f"[Warning] Error parsing parameter file: {e}. Using default parameters.")

    # Fallback to default if any parameters are missing
    from config import DEFAULT_PARAMETERS
    for key, default_value in DEFAULT_PARAMETERS.items():
        if key not in parameters:
            print(f"[Warning] Missing parameter '{key}' in file. Using default value: {default_value}")
            parameters[key] = default_value

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
