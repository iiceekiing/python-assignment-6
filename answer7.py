"""
    Task 7:
    Write a function that accepts three numbers as parameters
    and returns the largest number.
"""


def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

num1 =  float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))

print(f"the largest number is: {find_max_number(num1, num2, num3)}")
