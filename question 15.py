import math

def sin(x,n):
    sum = 0
    for i in range(1, n + 1, 4):
        sum += (x ** i) / math.factorial(i)
    for i in range(3, n + 1, 4):
        sum -= (x ** i) / math.factorial(i)
    return sum
n = int(input("Enter n: "))
x = float(input("Enter x: "))
print("sin(",x,",",n,") = ", sin(x,n) )

