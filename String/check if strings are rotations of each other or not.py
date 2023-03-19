# Difficulty - Easy
from typing import *
from collections import deque

# Method - 1
class Solution:
    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False

        temp = s1*2

        if  temp.count(s2) > 0:
            return True
        return False


# Method - 2
    def areRotations_2(self, s1, s2):
        if len(s1) != len(s2):
            return False

        q1 = deque()
        for i in s1:
            q1.append(i)
        q2 = deque()
        for i in s2:
            q2.append(i)

        k = len(s1)
        while k!=0:
            x1 = q2.pop()
            q2.appendleft(x1)
            if q1 == q2:
                return True
            k -= 1

        return False


s1 = "ABCD"
s2 = "CDAB"
rot = Solution()
print(rot.areRotations(s1, s2))
print(rot.areRotations_2(s1, s2))
