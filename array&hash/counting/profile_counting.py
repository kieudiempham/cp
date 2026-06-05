import cProfile
from counting import max_freq

def test():
    nums = [1] * 1000000
    max_freq(nums)

cProfile.run('test()')