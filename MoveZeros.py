nums=list(map(int,input("enter the nums : ").split()))

non_zeros=[]

for i in range(len(nums)):
    if nums[i]!=0:
        non_zeros.append(nums[i])
        
zerolen=(len(nums)-len(non_zeros))

non_zeros.extend([0]*zerolen)

print(non_zeros)

#in-place
#  index = 0 
        
#         for num in nums:
#             if num != 0:
#                 nums[index] = num
#                 index += 1
        
#         for i in range(index, len(nums)):
#             nums[i] = 0
