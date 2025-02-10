a = list(map(int,input("Enter the elements:").split()))
print("List:", a)

target=int(input("enter the target:"))
print("Target:", target)


if(target in a):
    print(a.index(target))

else:
    index1=len(a)
    
    for i in range(len(a)):
        
            
        if(target<a[i]):
            index1=i
            break
        
    a.insert(index1, target)
    
    print("Inserting at:", index1)
    print("Updated List:", a)