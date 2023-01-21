#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for c in s:
            if c not in first.keys(): first[c] = 0
            first[c] += 1
        for c in t:
            if c not in second.keys(): second[c] = 0
            second[c] += 1
        return first == second
# @lc code=end

