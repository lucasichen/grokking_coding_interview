#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        F1, F2, window_start = [0] * 26, [0] * 26, 0
        return_arr = []
        k = len(p)
        for i in p:
            F1[ord(i)-97] += 1

        for window_end in range(len(s)):
            F2[ord(s[window_end])-97] += 1

            if window_end - window_start + 1 == k:

                if F1 == F2: return_arr.append(window_end-k+1)
                F2[ord(s[window_start])-97] -= 1
                window_start += 1
        return return_arr



# @lc code=end

