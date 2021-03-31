def temp(f):
    c = (f - 32) * (5 / 9)
    print(f, "Fahrenheit is equal to", c, "degree celsius")

new = 0
while new == 0:
    f = float(input("Enter the temperature in Fahrenheit:"))
    temp(f)
    new = int(input("Enter 0 to continue. Enter any other Number to Exit: "))

