from typing import *

# [-2,1,-3,5,6,-1]

def neg_pos_partiton(arr: List) -> List:
    j = 0
    l = len(arr)
    for i in range(l):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = [2,1,-3,1, 2,-1,5,6,-1]
print(neg_pos_partiton(arr))
