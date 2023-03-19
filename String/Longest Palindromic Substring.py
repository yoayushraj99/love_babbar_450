# Difficulty - Medium

# The main Concept used in this question is that Palindrome can also be checked by going from inside-out instead out ouside to inside.
# Start from the centre of the substring and go outwards.

from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0
        resLen = 0

        for i in range(len(s)):
            # Odd length Palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Here r-l+1 is the length of the palindromic substring
                if resLen < (r - l + 1):
                    res_l = l
                    res_r = r
                    resLen = r - l + 1

                l -= 1
                r += 1

            # Even length Palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    res_l = l
                    res_r = r
                    resLen = r - l + 1

                l -= 1
                r += 1

        return s[res_l:res_r + 1]
