nums = list(map(int, input("Enter the array: ").split()))

sort=sorted(nums)
trail =[]
missing = []

maxi=max(nums)
mini=min(nums)

print(sort)
print(maxi)
print(mini)

for i in range(mini,maxi+1):
    trail.append(i)
    
print(trail)    

for i in range(len(sort)):
    if sort[i]==trail[i]:
        continue
    else:
        missing.append(trail[i])
        
print(missing[0])

# return sum(range(len(nums)+1))-sum(nums)

# n = len(nums)
#          expected_sum = n * (n + 1) // 2
#          actual_sum = sum(nums)
#          return expected_sum - actual_sum


        # num_set = set(nums)  # Store all unique numbers from the input
        # n = len(nums)  # Total numbers expected in range [1, n]

        # missing_numbers = []  # List to store missing numbers

        # # Check for missing numbers in the range [1, n]
        # for i in range(1, n + 1):
        #     if i not in num_set:
        #         missing_numbers.append(i)  # Add missing numbers to the list

        # return missing_numbers