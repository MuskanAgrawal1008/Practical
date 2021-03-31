def fact(num):
    sum = 1
    while num > 0:
        sum *= num
        num -= 1
    print(sum)

num = int(input("Enter a number:"))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("Factorial of", num, "is:", end="")
    fact(num)
