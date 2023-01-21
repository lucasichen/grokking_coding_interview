#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        par= {'{':'}',
             '[':']',
             '(':')'}
        stack = []
        for b in s:
            if b in par: stack.append(b)
            elif stack == []: return False
            elif par[stack[-1]] == b: stack.pop()
            else: return False
        return stack == []
# @lc code=end

