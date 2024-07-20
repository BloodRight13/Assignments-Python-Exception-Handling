# Task 1
try:
    temperture_fahrenheit = int(input("What is the current tempature in your location? (Please enter a number) "))
except ValueError:
    pass
# Task 2
try:
    temperture_celsius = (temperture_fahrenheit - 32) *59
except NameError:
    print("For the system to work properly please enter a number.")
# Task 3
else:
    print(str(temperture_fahrenheit) + " degrees Fahrenheit is " + str(temperture_celsius) + " degrees Celsius.")
# Task 4
finally:
    print("Thank you for using our weather forcast system. Have a wonderful day.")