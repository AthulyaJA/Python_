a=[1,2,3,4,5,6,7,8,9]
p=[]
q=[]
for i in range(len(a)):
    if a[i]%2==0:
        p.append(a[i])
    else:
        q.append(a[i])
print(p)
print(q)