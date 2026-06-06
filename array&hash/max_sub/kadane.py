nums = [-2,1,-3,4,-1,2,1,-5,4]
class maxSubArray:
    def kadane(self, nums):
        current = 0
        best = float('-inf')
        for i in range(0, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(current, best)
        return best

solver = maxSubArray()
solver.kadane(nums)
print(solver.kadane(nums))