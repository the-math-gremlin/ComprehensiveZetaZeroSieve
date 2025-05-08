import os

def load_parameters(filepath):
    # Load the sieve parameters from a text file
    parameters = {}
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "=" in line:
                key, value = line.split("=")
                parameters[key.strip()] = float(value.strip())
    return parameters
