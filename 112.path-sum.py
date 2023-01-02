#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = [(root,0)]
        while stack:
            node, parent_sum = stack.pop()
            if node:
                new_sum = parent_sum + node.val
                if not node.left and not node.right and new_sum == targetSum: return True
                if node.right: stack.append((node.right, new_sum))
                if node.left: stack.append((node.left, new_sum))
        return False
# @lc code=end

