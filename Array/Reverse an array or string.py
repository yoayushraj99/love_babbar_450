# Method-1

def reverse1(arr):
    l = len(arr)
    for i in range(l // 2):
        arr[i], arr[l - i - 1] = arr[l - i - 1], arr[i]
    return arr


print(reverse1([1, 2, 3, 4, 5]))


# Method-2

def reverse2(arr):
    return arr[::-1]
