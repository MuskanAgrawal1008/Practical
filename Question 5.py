def odd_even(x):
    if x%2 == 0:
        print(x, "is an even number")
    else:
        print(x, "is a odd number")

def prime(y):
    if y > 1:
        for i in range(2, y):
           if y % i == 0:
            print(y,"is not a prime number")
            break
           else:
            print(y, "is a prime number")
            break
    else:
        print(num, "is a prime number")

new = 0
while new == 0:
    num = int(input("Enter a number: "))
    op = int(input("Find 1. Odd or Even   2. Prime\n"))
    if op == 1:
        odd_even(num)
    elif op == 2:
        prime(num)
    else:
        print("Invalid option")
    new = int(input("Enter 0 to continue. Enter any other Number to Exit: "))
