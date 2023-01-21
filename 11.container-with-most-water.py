#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right,maxArea = 0, len(height)-1, 0
        while left < right:
            width = right - left
            maxArea = max(maxArea, min(height[left],height[right])*width)
            if height[left] <= height[right]: left += 1
            else: right -= 1
        return maxArea
# @lc code=end

