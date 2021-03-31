greatest = int(input("Enter a number :"))
n = 0
while n==0:
    num = int(input("Enter another num or Enter -1 to exit :"))
    if num > greatest:
        greatest = num
    elif num == -1:
        break
print("Maximum of given numbers is:",greatest)
