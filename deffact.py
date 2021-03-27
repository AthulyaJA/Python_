def fact(a):
    fact=1
    a=int(input("enter the number"))
    for i in range(1,a+1):
        fact=fact*i
    return fact
#fact(a)
print(fact(fact))