#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            word = ''.join(sorted(s))
            if word not in res: res[word] = []
            res[word].append(s)
        return res.values()
# @lc code=end

