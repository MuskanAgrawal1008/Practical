def rev(x):
    reverse = str(a) + str(b)
    print(reverse)

def add(x):
    sum = a+b
    print(sum)

new = 0
while new == 0:
    num = int(input("Enter the number: "))
    a = num % 10
    b = (num - a) // 10
    op = int(input("Choose the Opton\n1. Reverse the number      2. Print the sum of digits\n "))

    if op == 1:
        rev(num)
    elif op == 2:
        add(num)
    else:
        print("Invalid option")
    new = int(input("Enter 0 to continue. Enter any other Number to Exit: "))