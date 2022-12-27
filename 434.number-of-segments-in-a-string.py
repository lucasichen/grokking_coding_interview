#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in s.split(" "):
            if i != "": count += 1
        return count
# @lc code=end

