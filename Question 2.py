def sum(a,b):
    return(a+b)

def diff(a,b):
    return a-b

def prod(a,b):
    return a*b

def div(a,b):
    return a/b

def floordiv(a,b):
    return a//b

def mod(a,b):
    return a%b
number = 0
while number == 0 :
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = input(" Choose an operator: \na: +   b: -   c: *   d: /   e: //   f: % \nYour Choice: ")

    if z == "a":
        print("Sum is: ", sum(x, y))
    elif z == "b":
        print("Difference is: ", diff(x, y))
    elif z == "c":
        print("Product is: ", prod(x, y))
    elif z == "d":
        print("Division is: ", div(x, y))
    elif z == "e":
        print("Floor division is: ", floordiv(x, y))
    elif z == "f":
        print("Modulus is: ", mod(x, y))
    else:
        print("Enter Valid option")
    number = int(input("Enter 0 to continue. Enter Any Other Number to Exit "))
