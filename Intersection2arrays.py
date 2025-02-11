nums1=list(map(int,input("enter the nums : ").split()))
nums2=list(map(int,input("enter the nums : ").split()))

nums3=set(nums1)
nums4=set(nums2)

ans=nums3.intersection(nums4)

print(list(ans))