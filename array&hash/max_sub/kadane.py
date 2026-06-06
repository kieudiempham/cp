nums = [-5,-2,-8]
class maxSubArray:
    def kadane(self, nums):
        current = nums[0]
        best = nums[0]
        best_start = 0
        best_end = 0
        temp_start = 0
        #numbers = [0] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > (current + nums[i]):
                current = nums[i]
                temp_start = i
                #numbers[i] = 1
            else:                
                current = current + nums[i]
                #numbers[i] = numbers[i-1] + 1
            if current > best:
                best = current
                best_start = temp_start
                best_end = i
            elif current == best:
                current_len = i - temp_start + 1
                best_len = best_end - best_start + 1
                if current_len > best_len:
                    best_start = temp_start
                    best_end = i        
        return best, nums[best_start:best_end+1], current

solver = maxSubArray()
print(solver.kadane(nums))