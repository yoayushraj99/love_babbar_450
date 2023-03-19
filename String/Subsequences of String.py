# Difficulty - Medium
# You are given a string 'STR' containing
# lowercase English letters from a to z inclusive.
# Your task is to find all non-empty possible subsequences of 'STR'.

from typing import *


def subsequences(str):
    # Write your code here
    ans = []

    def subUtil(index, output=""):
        if index >= len(str):
            if len(output) > 0:
                ans.append(output)
            return

        # Exclude
        subUtil(index + 1, output)

        # Include
        output += str[index]
        subUtil(index + 1, output)

    subUtil(0)
    return ans
