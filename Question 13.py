def marks(n):
    if n > 0.9:
        print("Grade A")
    elif 0.90>= n > 0.80:
        print("Grade B")
    elif 0.80>= n > 0.70:
        print("Grade C")
    elif 0.70>= n > 0.60:
        print("Grade D")
    else:
        print("Grade E")

a = int(input("Enter number of subject 1:" ))
b = int(input("Enter number of subject 2:" ))
c = int(input("Enter number of subject 3:" ))
d = int(input("Enter number of subject 4:" ))
e = int(input("Enter number of subject 5:" ))
sum = a+b+c+d+e
avg = sum/500
marks(avg)


