nums = [1,1,2]

sortnums = sorted(set(nums))
if len(sortnums)>=3:
    print(sortnums)
    print(sortnums[-3])

else:
    print(sortnums[-1])