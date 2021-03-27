rows=4
for i in range(4):
    for j in range(4):
        if(  i==0 or i==1 or   j==0 or j==3): 
            print("c",end=" ")
        else:
            print(" ",end=" ")
    print("\n")    