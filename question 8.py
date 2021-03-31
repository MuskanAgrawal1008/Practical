new = 0
while new == 0:
    num = input("Enter the number to check if it is armstrong or not : ")
    a = 0
    for i in range(0, len(num)):
        a += int(num[i]) ** len(num)
    val = str(a)
    if val == num:
        print("Its an armstrong number")
    else:
        print("Its not an armstrong number")
    new = int(input("Enter 0 to check any other number. Enter any other Number to Exit: "))


