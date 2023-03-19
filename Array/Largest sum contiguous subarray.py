# Use Kadane's Algorithm

from typing import *

def max_subarray_sum(arr: List) -> int:
    current_sum = float('-inf')
    best_sum = float('-inf')

    for num in arr:
        current_sum = max(current_sum+num, num)
        best_sum = max(current_sum, best_sum)

    return best_sum


print(max_subarray_sum([-1,1,2,5,-5,0,2]))
