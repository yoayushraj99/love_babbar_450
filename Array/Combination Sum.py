# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

from typing import *


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def utilSum(nums, target, output, index, ans):
        if target == 0:
            ans.append(output.copy())
            return
        if index >= len(nums):
            return

        # take if the target is greater than the element
        element = nums[index]
        if element <= target:
            output.append(element)
            utilSum(nums, target - element, output, index, ans)
            output.pop()

        # backtracking
        utilSum(nums, target, output, index + 1, ans)

    ans = []
    utilSum(candidates, target, [], 0, ans)
    return ans


print(combinationSum([2, 3, 6, 7], 7))
