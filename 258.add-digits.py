#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        _sum = str(num)
        if len(_sum) == 1: return num
        while len(_sum) != 1:
            res = 0
            for numb in _sum:
                res += int(numb)
            _sum = str(res)
        return int(_sum)

# @lc code=end

