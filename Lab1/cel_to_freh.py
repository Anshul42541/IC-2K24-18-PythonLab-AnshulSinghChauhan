# Take temperature in Celsius as input. 
# Convert it to a number, then compute and print the Fahrenheit value.
# Formula: F = (C * 9/5) + 32

temp = int(input("Enter temperature in Celcius : "))

F = (temp * 9/5) + 32  #Calculating fahren

print(f"{temp} degree celcius is equal to {F} fahrenheit.") 
