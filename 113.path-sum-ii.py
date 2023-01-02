#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        stack = [(root, 0, [])]
        ans_arr = []
        while stack:
            node, parent_sum, path = stack.pop()
            _sum = parent_sum + node.val
            if not node.left and not node.right and _sum == targetSum: ans_arr.append(path + [node.val])
            if node.right: stack.append((node.right, _sum, path + [node.val]))
            if node.left: stack.append((node.left, _sum, path + [node.val]))
        return ans_arr
# @lc code=end

