def merge_sort(arr1, arr2, n, m):
    # code here
    merged_array = []
    i = j = 0

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    return merged_array + arr1[i:] + arr2[j:]


print(merge_sort([1, 3, 5, 7], [0, 2, 6, 8, 9], 4, 5))
