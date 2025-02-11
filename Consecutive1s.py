nums=list(map(int,input("enter the nums : ").split()))
count=0
rel=[]
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
        print(count)
    else:
        rel.append(count)
        count=0
rel.append(count)
print( max(rel))
print(rel)
