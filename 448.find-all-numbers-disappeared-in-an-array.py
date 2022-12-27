#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_dict = {}
        res = []
        for num in nums: my_dict[num] = 1
        for i in range(1,len(nums)+1):
            try:
                if my_dict[i]: continue
            except Exception:
                res.append(i)
        return res
# @lc code=end

