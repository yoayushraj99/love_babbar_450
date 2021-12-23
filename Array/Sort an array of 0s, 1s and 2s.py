# Given array only has 0s, 1s, 2s like [0, 1, 2, 0, 1].
# We have to sort it without using sorting algorithm.

def sort012(arr, n):
    low = 0
    high = n-1
    mid = 0

    while mid <= high:
        if arr[mid]==0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print(arr)


sort_012 = sort012([0,1,2,1,0,1,2,1,2,0], 10)
