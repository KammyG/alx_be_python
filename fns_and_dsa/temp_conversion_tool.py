# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Define conversion functions
def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# User interaction and input validation
def main():
    try:
        # Prompt for temperature
        temperature = float(input("Enter the temperature to convert: "))

        # Prompt for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert and display the result based on the unit
        if unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        # Handle invalid input for temperature or unit
        print(f"Error: {e}. Please ensure the temperature is numeric and the unit is 'C' or 'F'.")

# Execute the script
if __name__ == "__main__":
    main()

