# Difficulty - Hard

# Given two strings A and B, the task is to convert A to B if possible.
# The only operation allowed is to put any character from A and insert it at front.
# Find if it’s possible to convert the string. If yes, then output minimum
# no. of operations required for transformation.

from typing import *


class Solution:
    def minOps(self, s1, s2):
        m = len(s1)
        n = len(s2)

        if m != n:
            return -1

        count = [0] * 256

        for i in range(n):
            count[ord(s1[i])] += 1
        for i in range(n):
            count[ord(s2[i])] -= 1
        for i in range(256):
            if count[i]:
                return -1

        # This part calculates the number of operations required
        i = n-1
        j = n-1

        res = 0

        while i >= 0:
            # if there is a mismatch, then keep incrementing
            # result 'res' until B[j] is not found in A[0..i]
            while i >= 0 and s1[i] != s2[j]:
                i -= 1
                res += 1
            # if A[i] and B[j] match
            if i >= 0:
                i -= 1
                j -= 1

        return res


A = "EACBD"
B = "EBADC"
x = Solution()
print ("Minimum number of operations required is " + str(x.minOps(A,B)))

# Time Complexity: O(n), please note that i is always decremented (in while loop and in if),
# and the for loop starts from n-1 and runs while i >= 0.
