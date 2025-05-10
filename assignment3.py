

# Task 1: Calculate Factorial Using a Function 
n = int(input("ENTER A NUMBER: "))
def factorial(n):
    if  n < 2 :
        return(1)
    else: 
        return(n*factorial(n-1)) 

factorial_result = factorial(n)
print("Factorial of", n, "is:", factorial_result)

# Task 2: Using the Math Module for Calculations
import math

number = float(input("Enter a number for math calculations: "))

square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

print(f"Square root of {number} is: {square_root}")
print(f"Natural logarithm of {number} is: {natural_log}")
print(f"Sine of {number} (in radians) is: {sine_value}")

