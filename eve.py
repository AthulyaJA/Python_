l=[]
e=[]
a=int(input("enter the range"))
for i in range(0,a+1):
    b=int(input())
    l.append(b)
print(l)
def even(e):
    for i in range(0,a+1):
        if(l[i]%2==0):
            e.append(l[i])
    return e
print(even(e))
        
    