import math
new = 0
while new == 0:
    a = int(input("Enter coefficient of x^2: "))
    if a == 0:
        print("coefficient of x^2 cannot be 0")
    else:
        b = int(input("Enter coefficient of x: "))
        c = int(input("Enter coefficient of 1: "))

        d = b ** 2 - (4 * a * c)
        if d < 0:
            re = (- b) / 2 * a
            first_im = (math.sqrt(-d)) / 2 * a
            sec_im = (-math.sqrt(-d)) / 2 * a

            print("First root is :" + str(re) + "+" + str(first_im) + "i and Second root is" + str(re) + str(
                sec_im) + "i")

        else:
            first = (- b + math.sqrt(d)) / 2 * a
            sec = (- b - math.sqrt(d)) / 2 * a
            print("First root is:", first, "and second root is", sec)

        new = int(input("Enter 0 to continue. Enter any other Number to Exit: "))

