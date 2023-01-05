#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numL = len(nums)
        res = []
        perms = deque()
        perms.append([])
        for curr in nums:
            n = len(perms)
            for _ in range(n):
                old_perm = perms.popleft()
                for j in range(len(old_perm)+1):
                    new_perm = list(old_perm)
                    new_perm.insert(j, curr)
                    if len(new_perm) == numL: res.append(new_perm)
                    else: perms.append(new_perm)
        return res
# @lc code=end

