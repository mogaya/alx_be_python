FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    converted_celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted_celsius

def convert_to_fahrenheit(celsius):
    converted_fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return converted_fahrenheit

temperature = float(input("Enter the temperature to convert: "))
scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().capitalize()

try:
    if scale == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif scale == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")