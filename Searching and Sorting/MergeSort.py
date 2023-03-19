# Difficulty - 
from typing import *

class Solution:
    def mergeSort(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            # Two iterators for traversing the two halves
            i = j = 0
            # Iterator for mail list
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]
                    j+=1
                k+=1

            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1

            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1

    def printList(self, arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    x  = Solution()
    x.printList(arr)
    x.mergeSort(arr)
    print("Sorted array is: ", end="\n")
    x.printList(arr)
