import copy
def removeDuplicates(nums,val):
    nums[:]=list(filter((lambda x: nums[x]!=val),nums))
    print(nums)
    return len(nums)
nums=[0,1,2,2,3,0,4,2]
val=2
l=removeDuplicates(nums,val)
"""for i in range(l):
    print(nums[i])"""
print(nums)