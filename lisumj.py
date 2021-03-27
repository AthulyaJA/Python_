x=int(input("enter the limit"))
print("enter {}elemetns".format(x))
l=[]
for i in range(x):
    n=int(input())
    l.append(n)
def add(a):
    s=0
    for i in a:
        s=s+i
    return s
print(add(l))