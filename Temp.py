# Program to convert the Temperature to and from Celsius and fahrenheit
Fahrenheit = float(input("Enter a temperature in Fahrenheit:"))
Celsius = (Fahrenheit - 32) * 5.0/9.0
print("Temperature:", Fahrenheit, "Fahrenheit = %0.2f" %Celsius, "C")

Celsius = float(input("Enter a temperature in celsius: "))
Fahrenheit = 9.0/5.0 * Celsius + 32
print("Temperature:", Celsius, "Celsius = %0.2f" %Fahrenheit, "F")