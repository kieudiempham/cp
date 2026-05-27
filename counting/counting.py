import logging 
import time

logging.basicConfig(level=logging.INFO)
start_time = time.time()
nums = [1,1,1,2,3]
def max_freq(nums): 
    count = {}
    max_freq = 0
    a = 0
    for num in nums:
        logging.info(f"Current number: {num}")
        if num in count:
            count[num] += 1
        else:        
            count[num] = 1
        logging.info(f"Current count: {count}")

    for num in count:
        if count[num] > max_freq:
            max_freq = count[num]
            a = num
    return a
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")