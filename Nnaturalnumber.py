def sum(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print("Sum of first n natural number is  : ", sum)

print(" To Find Sum of n natural number. ")
n = int(input("Enter the value of n: "))
sum(n)
