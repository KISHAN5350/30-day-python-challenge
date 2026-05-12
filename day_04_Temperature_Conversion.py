# Experiment 4: Temperature Conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
fahr = float(input("Enter temperature in Fahrenheit: "))
cel = (fahr - 32) * 5/9
print(f"{fahr}°F = {cel:.2f}°C")