from typing import *


def find_kth_largest(arr: List, l: int, r: int, k: int) -> int:
    k = len(arr) - k

    def quickSelect(l, r):
        pivot = arr[r]
        i = l - 1

        for j in range(l, r):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[r], arr[i + 1] = arr[i + 1], arr[r]
        p = i + 1

        if k < p:
            return quickSelect(l, p - 1)
        elif k > p:
            return quickSelect(p + 1, r)
        else:
            return arr[p]

    return quickSelect(l, r)


print(find_kth_largest([1, 4, 2, 5, 10, 56, 12], 0, 6, 1))
