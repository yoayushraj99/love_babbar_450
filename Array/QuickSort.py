# Implementation Details
# 1. Choosing pivot
#       -> Random Element(Mostly the last element)
#       -> median of three
#
# Chose a pivot(generally we take the last element as pivot) then
# using partition fuction put the elements lesser than pivot to the left of the pivot and
# the elements larger than the pivor to the right of the pivot.
# Then do this recusively.

# 2. Dealing with duplicates
#       -> Use 3-way quicksort

from typing import *

def partition(arr:List, l:int, r:int) -> int:
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def qsort(arr:List, l:int, r:int) -> List:
    if l >= r:
        return
    p = partition(arr, l, r)
    qsort(arr, l, p-1)
    qsort(arr, p+1, r)
    return arr


print(qsort([0,20,40,30,60,10,90],0, 6))
