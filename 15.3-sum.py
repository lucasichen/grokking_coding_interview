#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = {}
        arr = []
        for x in range(len(nums)):
            for i,value in enumerate(nums):
                remaining = target - value
                if remaining in seen:
                    arr.append((x, i,seen[remaining]))
                seen[value] = i
        print(arr)
        return arr
# @lc code=end

