list=[]
even=[]
odd=[]
a=int(input("enter the range"))
for i in range(0,a+1):
    b=int(input())
    list.append(b)
print(list)
for i in range(0,a+1):
    if(list[i]%2==0):
        even.append(list[i])
    else:
        odd.append(list[i])
print(even)
print(odd)
