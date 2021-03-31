def my_mean(sum):
    mean = sum / len(list)
    print("Mean:", mean)

list = []
n = int(input("Number of elements in the list: "))
sum= 0
for i in range(0,n):
    ele = float(input("enter number: "))
    list.append(ele)
    sum+=ele
my_mean(sum)