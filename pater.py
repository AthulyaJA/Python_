rows=6
for i in range(6):
    for j in range(6):
        if(i==0 or i==rows - 1 or j==0 or j==rows - 1): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")    