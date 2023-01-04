#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            res = self.path_from_source(node, res, targetSum)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res
    
    def path_from_source(self, root, res, psum):
        if not root: return res
        stack = [(root,root.val)]
        while stack:
            node, parent_sum = stack.pop()
            if parent_sum == psum: res += 1
            if node.left: stack.append((node.left, parent_sum + node.left.val))
            if node.right: stack.append((node.right, parent_sum + node.right.val))
        return res
# @lc code=end

