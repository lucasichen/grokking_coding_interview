#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag,ran = [0]*26, [0]*26
        for i in range(len(magazine)):
            c = ord(magazine[i])-97
            mag[c] += 1
        for i in range(len(ransomNote)):
            c = ord(ransomNote[i])-97
            ran[c] += 1
        for i in range(26):
            if ran[i] == 0: pass
            elif ran[i] > mag[i]: return False
        return True
# @lc code=end

