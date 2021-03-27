a=int(input("enter the range"))
for i in range(1,a+1):
    for j in range(1,a+1):
        x=i*j
        print("{}*{}={}\t".format(i,j,x))
        