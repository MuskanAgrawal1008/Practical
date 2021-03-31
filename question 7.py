new = 0
while new== 0:
    word = input("Enter a character:")
    for i in word:
        print("Ascii code of", i, "is:", ord(i))
    code = int(input("Enter an Ascii code:"))
    print("Character value of", code, "is:", chr(code))
    new = int(input("Enter 0 to continue. Enter any other Number to Exit: "))


