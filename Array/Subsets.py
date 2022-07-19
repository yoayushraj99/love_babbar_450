# Difficulty - Medium
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import *


class Solution:
    def subsetsUtil(self, nums, output, index, ans):
        # Base Case
        if index >= len(nums):
            ans.append(output.copy())
            return

        # Include
        element = nums[index]
        output.append(element)
        self.subsetsUtil(nums, output, index + 1, ans)

        # Exclude
        output.pop()
        self.subsetsUtil(nums, output, index + 1, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.subsetsUtil(nums, [], 0, ans)
        return ans
