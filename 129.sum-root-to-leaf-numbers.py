#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [(root, 0)]
        _sum = 0
        while stack:
            node, parent_sum = stack.pop()
            parent_sum = 10 * parent_sum + node.val
            if not node.right and not node.left: _sum += parent_sum
            if node.right: stack.append((node.right, parent_sum))
            if node.left: stack.append((node.left, parent_sum))
        return _sum
# @lc code=end

