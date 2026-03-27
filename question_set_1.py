'''User Input & f-string
Take a user’s name and age as input and print:
Hello Rahul, you are 25 years old.'''

name = input("Please enter your name:")
age = input("Please enter your age:")
print(f"Hello {name}, you are {age} years old.")


'''Simple Calculator
Take two numbers and print their:
Sum
Difference
Product
using f-strings.'''
a = float(input("Enter number 1:"))
b = float(input("Enter number 2:"))
print(f"Sum:{a+b}")
print(f"Difference: {a-b}")
print(f"Product:{a*b}")