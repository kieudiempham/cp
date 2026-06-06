class Solution(object):
    def twoSum(self, nums, target):
        count = {}
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in count:
                return [count[x], i]
            count[nums[i]] = i
            
solver = Solution()
print(solver.twoSum([2, 7, 11, 15], 22))       