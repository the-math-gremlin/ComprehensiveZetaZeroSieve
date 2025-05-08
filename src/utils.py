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
        lines = file.readlines()
        for line in lines:
            if "=" in line:
                key, value = line.split("=")
                parameters[key.strip()] = float(value.strip())
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
