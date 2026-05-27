from counting import max_freq
import timeit

execution_time = timeit.timeit(
    stmt="max_freq([1]*1000 + [2]*500 + [3]*200)",
    setup="from counting import max_freq",
    number=100
)
print(f"Execution time: {execution_time} seconds")