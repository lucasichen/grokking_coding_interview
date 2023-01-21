#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2: return n
        start, maxLength, seen = 0, 0,{}
        for end in range(n):
            r = s[end]
            if r not in seen: seen[r] = 0
            seen[r] += 1
            while seen[r] > 1:
                l = s[start]
                seen[l] -= 1
                start += 1
            maxLength = max(maxLength, end-start+1)
        return maxLength
# @lc code=end

