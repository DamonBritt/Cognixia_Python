import math
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number. NOT ZERO: "))
squareNum = num1 + num2

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def square(num):
    return math.sqrt(num)

print("The sum of your two numbers is", add(num1, num2))
print("The difference of your two numbers is", sub(num1, num2))
print("The product of your two numbers is", mult(num1, num2))
print("The quotient of your two numbers is", div(num1, num2))
print("The modulus of your two numbers is", mod(num1, num2))
print("The square root of the sum of your two numbers is",square(squareNum))