#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n
    
        # my_dict = {}
        # for num in nums: my_dict[num] = 1
        # for i in range(0,len(nums)+1):
        #     try:
        #         if my_dict[i]: continue
        #     except Exception:
        #         return i
# @lc code=end

