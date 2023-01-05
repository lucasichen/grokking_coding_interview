#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for curr in nums:
            for i in range(len(subsets)):
                sub = subsets[i] + [curr]
                subsets.append(sub)
        return subsets
# @lc code=end

