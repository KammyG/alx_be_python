def convert_to_celsius(fahrenheit):
  """Converts temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit.

  Returns:
      The temperature in Celsius.
  """
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """Converts temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature in Fahrenheit.
  """
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# Define global conversion factors (5/9 for F to C, 9/5 for C to F)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

while True:
  try:
    # Get user input for temperature and unit
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit not in ("C", "F"):
      raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    # Call appropriate conversion function based on unit
    if unit == "C":
      converted_temp = convert_to_fahrenheit(temperature)
      unit_label = "Celsius"
      converted_unit = "Fahrenheit"
    else:
      converted_temp = convert_to_celsius(temperature)
      unit_label = "Fahrenheit"
      converted_unit = "Celsius"

    # Display the converted temperature
    print(f"{temperature:.1f}°{unit_label} is {converted_temp:.1f}°{converted_unit}")
    break

  except ValueError as e:
    print(f"Error: {e}")
    print("Please enter a valid numeric value and unit (C or F).")
