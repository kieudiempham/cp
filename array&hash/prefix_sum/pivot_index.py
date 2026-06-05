nums = [1, 7, 3, 6, 5, 6]
prefix = [0] * (len(nums)+1)
result = 0
def pivotIndex(nums):
    for i in range(0, len(nums)):
        prefix[i+1] = prefix[i] + nums[i]

    for i in range(0, len(nums)):
        print(prefix[i], prefix[len(nums)] - prefix[i+1])
        if prefix[i] == prefix[len(nums)] - prefix[i+1]:
            return i
    return -1
print(pivotIndex(nums))