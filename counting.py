def max_freq(nums):
    count = {}
    max_freq = 0
    a = 0
    for num in nums:
        if num in count:
            count[num] += 1
        else:        count[num] = 1

    for num in count:
        if count[num] > max_freq:
            max_freq = count[num]
            a = num
    return a