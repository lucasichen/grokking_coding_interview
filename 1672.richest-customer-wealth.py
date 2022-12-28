#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = float("-inf")
        for account in accounts: max_w = max(max_w,sum(account))
        return max_w
# @lc code=end

