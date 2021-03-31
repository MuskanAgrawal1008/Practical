i = int(input("Enter no. of terms: "))
a= 0
b=1
count = 0
print("Fibonacci series upto",i,"number of terms is: ",end="")
while count<i:
    if i<0:
        print("Invalid input")
    elif i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        print(a, end="  ")
        c = a + b
        a = b
        b = c
    count+=1
