num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number. NOT ZERO: "))

def add(num1, num2):
    sum1 = num1 + num2
    return sum1

def sub(num1, num2):
    dif = num1 - num2
    return dif

def mult(num1, num2):
    prod = num1 * num2
    return prod

def div(num1, num2):
    quot = num1 / num2
    return quot

def mod(num1, num2):
    rem = num1 // num2
    return rem 

sum1 = add(num1, num2)
dif = sub(num1, num2)
prod = mult(num1, num2)
quot = div(num1, num2)
mod = mod(num1, num2)
print("The sum of your two numbers is", sum1)
print("The difference of your two numbers is", dif)
print("The product of your two numbers is", prod)
print("The quotient of your two numbers is", quot)
print("The modulus of your two numbers is", mod)