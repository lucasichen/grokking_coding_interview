#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        my_arr = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                my_arr[i] = nums[left]**2
                left += 1
            else:
                my_arr[i] = nums[right]**2
                right -= 1
        return my_arr
# @lc code=end

