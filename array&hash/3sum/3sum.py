class Solution(object):
    def threeSum(self, nums):
        count = {}
        results = set()
        for i in range(0, len(nums)):
            count[nums[i]] = i
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                x = 0 - nums[i] - nums[j]
                if x in count and count[x] > j:
                    triplet = sorted([nums[i], nums[j], x])
                    results.add(tuple(triplet))
        return [list(x) for x in results] 

solver = Solution()
print(solver.threeSum([-1, 0, 1, 2, -1, -4]))

        