# 
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        F1 = [0]*26
        F2 = [0]*26
        k = len(s1)
        for i in s1:
            F1[Solution.getOrd(i)] += 1
        for window_end in range(len(s2)):
            right_char = Solution.getOrd(s2[window_end])
            F2[right_char] += 1

            if window_end - window_start + 1 == k:
                start_ord = Solution.getOrd(s2[window_start])

                if F1 == F2: return True
                F2[start_ord] -= 1
                window_start += 1
        return False
    
    def getOrd(character):
        return ord(character) - 97
print(Solution().checkInclusion('abcdxabcde','abcdeabcdx'))
# @lc code=end

