list=[]
sum=0
a=int(input("enter the range"))
for i in range(0,a+1):
    b=int(input())
    list.append(b)
print(list)
for i in range(0,a+1):
    sum=sum+list[i]
print("sum={}".format(sum))