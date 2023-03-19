# Difficulty - Easy
from typing import *
from collections import defaultdict

class Solution:
    # Method - 1
    def areIsomorphic_1(self, str1, str2):
        if len(str1) != len(str2):
            return False
        # default dict to store mapping of characters
        d = defaultdict(chr)

        # Using a boolean list to mark visited characters in str2
        marked = [0 for i in range(26)]

        for i in range(len(str1)):
            s1 = str1[i]
            s2 = str2[i]
            # if s1 is seem first time in dict
            if s1 not in d:

                # if current character of str2 is already seem
                # Then one to one mapping is not possible
                if marked[ord(s2) - ord('a')]:
                    return False
                else:
                    # Marking current character if str2 as visited
                    marked[ord(s2) - ord('a')] = 1
                    # Store mapping of current characters
                    d[s1] = s2

            # if s1 is already in default dict then
            # check if previous appearance mapped to same character of str2
            else:
                if d[s1] != s2:
                    return False

        return True

    # Method-2
    def areIsomorphic_2(self, str1, str2):
        if len(str1) != len(str2):
            return 0

        dic1 = {}
        dic2 = {}

        for i in range(len(str1)):
            if str1[i] not in dic1:
                dic1[str1[i]] = str2[i]
            else:
                if dic1[str1[i]] != str2[i]:
                    return 0

        for i in range(len(str2)):
            if str2[i] not in dic2:
                dic2[str2[i]] = str1[i]
            else:
                if dic2[str2[i]] != str1[i]:
                    return 0
        if len(dic1) != len(dic2):
            return 0
        return 1


x = Solution()
print(x.areIsomorphic_1('aab', 'xyz'))
print(x.areIsomorphic_2('aab', 'xyz'))
