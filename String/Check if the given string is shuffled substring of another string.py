# Difficulty - Easy

# Given strings str1 and str2. The task is to find if str1 is a substring in the shuffled form of str2 or not. Print
# “YES” if str1 is a substring in shuffled form of str2 else print “NO”.
#
# Example
#
# Input: str1 = “onetwofour”, str2 = “hellofourtwooneworld”
# Output: YES
# Explanation: str1 is substring in shuffled form of str2 as
# str2 = “hello” + “fourtwoone” + “world”
# str2 = “hello” + str1 + “world”, where str1 = “fourtwoone” (shuffled form)
# Hence, str1 is a substring of str2 in shuffled form.

from typing import *


class Solution:
    # Method - 1 (Naive Solution)

    def isShuffledSubstring(self, s1, s2):
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1 = sorted(s1)

        for i in range(m):
            if i+n-1 >= m:
                return False

            str = ""

            for j in range(n):
                str += s2[i+j]

            str = sorted(str)

            if str == s1:
                return True

        return False

    # Method - 2 (Efficient Solution)
    def isShuffledSubstring_2(self, s1, s2):
        # Code here
        pass


# Input str1 and str2
Str1 = "geekforgeeks"
Str2 = "ekegorfkeegs"

a = Solution().isShuffledSubstring(Str1, Str2)
if (a):
    print("YES")
else:
    print("NO")
