#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        k,left = 0,0
        
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                k += 1              # the number of non-duplicates
                nums[k] = nums[right]
                left = right
        return k+1
        
# @lc code=end

