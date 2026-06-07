class Solution(object):
    def findPeakElement(self, nums):
        for i in range(0, len(nums)):
            if (i == 0 or nums[i] > nums[i-1]) and (i == len(nums)-1 or nums[i] > nums[i+1]):
                return i
solver = Solution()
print(solver.findPeakElement([1, 2, 3, 4, 5, 6, 4, 8, 9]))