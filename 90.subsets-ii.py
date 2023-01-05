#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        start, end = 0, 0
        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start = end + 1
            end = len(subsets) - 1
            for j in range(start, end + 1):
                sub = subsets[j] + [nums[i]]
                subsets.append(sub)
        return subsets
# @lc code=end

