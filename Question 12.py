def palo(s):
    j = 1
    for i in range(0, (len(s))//2):
        if s[i] == s[i - j]:
            j += 2
            return True
        else:
            return False
new = 0
while new == 0:
    s = input("Enter a string: ")
    if (palo(s) == True):
        print(s, "is a palindrome word")
    else:
        print(s, "is not a palindrome word")
    new = int(input("Enter 0 to continue. Enter any other Number to Exit: "))

