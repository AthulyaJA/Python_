def swap(a,b):
    #temp=0
    temp=a
    a=b
    b=temp
    return a,b
a=int(input("enter the first"))
b=int(input("enter the second"))
swap(a,b)
print(a,b)

