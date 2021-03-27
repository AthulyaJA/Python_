R1 = int(input("Enter the number of rows:")) 
C1 = int(input("Enter the number of columns:"))
R1 = int(input("Enter the number of rows:")) 
C1 = int(input("Enter the number of columns:")) 
  
matrix = [][] 
print("Enter the entries rowwise:") 
  
 
for i in range(R1):          
    a =[] 
    for j in range(C):      
         a.append(int(input())) 
    matrix.append(a) 
  
 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 