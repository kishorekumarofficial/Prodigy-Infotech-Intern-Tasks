def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K.")
        
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        
    else:
        print("Invalid unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    print("Welcome to the Temperature Converter!")
    
    try:
        # Get the temperature value from the user
        temperature = float(input("Enter the temperature value: "))
        
        # Get the unit of the input temperature
        unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        
        # Call the conversion function
        convert_temperature(temperature, unit)
    
    except ValueError:
        print("Invalid input! Please enter a valid temperature value.")

# Run the program
main()
