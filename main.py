import math

# Functions to calculate the pH of an acid 
def calculate_pH_acid(concentration_acid):
    return -math.log10(concentration_acid)

# Functiosn to calculate the pH of a base
def calculate_pH_base(concentration_base):
    pOH = -math.log10(concentration_base)
    return 14 - pOH

# Function that implements the calculations - will ask the user if the solution is an acid or a base and proceed accordingly. 
def main():
    try:

        # Getting the concentration of the substrance 
        concentration = float(input("Enter the concentration of the substance in moles per liter (M): "))
        while concentration <= 0:
            print("Concentration should be a positive number.")
            concentration = float(input("Enter the concentration of the substance in moles per liter (M): "))

        # Asking the user wether the substance is an acid or a base 
        substance_type = input("Is the substance an acid or a base? ").lower()

        while substance_type != "acid" and substance_type != "base":
            print("Please enter 'acid' or 'base' for the program to continue") 
            substance_type = input("Is the substance an acid or a base? ").lower()

        # Incorporation of the previously created functions to calculate and return the pH to the user 
        if substance_type == "acid":
            pH = calculate_pH_acid(concentration)
            print(f"The pH of the acid solution is: {pH:.2f}")
        elif substance_type == "base":
            pH = calculate_pH_base(concentration)
            print(f"The pH of the base solution is: {pH:.2f}")

    except ValueError:
        print("Please enter a valid number for the concentration.")
