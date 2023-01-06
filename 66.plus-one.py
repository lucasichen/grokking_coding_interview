#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            j = 0
            n = len(digits)
            mark = False
            for i in range(n)[::-1]:
                j = i
                digits[j] += 1
                if digits[j] == 10:
                    digits[j] = 0
                if digits[j] != 10 and digits[j] != 0: 
                    mark = True
                    break
            if not mark: digits.insert(j,1)
        else: digits[-1] += 1
        return digits
# @lc code=end

