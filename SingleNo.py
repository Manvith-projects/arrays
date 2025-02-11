from collections import Counter

nums=list(map(int,input("enter the nums : ").split()))

print(nums)

ans=[]

count=Counter(nums)
for key,value in count.items():
    if value==1:
        print(key)