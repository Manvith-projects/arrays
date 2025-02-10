n= int(input("enter the no.of rows"))

triangle=[[1]]#Row 1

for i in range(1,n):
    prev_row=triangle[-1]
    new_row=[1]
    
    for j in range(len(prev_row)-1):
        new_row.append(prev_row[j]+ prev_row[j+1])
        
    new_row.append(1)
    triangle.append(new_row)
    
print("Pascal Triangle:",triangle)