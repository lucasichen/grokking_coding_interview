#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node: return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            res = max(res, left + right + node.val)
        
            return max(left + node.val, right + node.val)
        dfs(root)
        return res
    
    # passes 93/94
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0
    #     stack = [root]
    #     res = -float('inf')
    #     while stack:
    #         node = stack.pop()
    #         left = max(self.source_path(node.left), 0)
    #         right = max(self.source_path(node.right),0)
    #         if node.left: stack.append(node.left)
    #         if node.right: stack.append(node.right)
    #         res = max(res, left + right + node.val)
    #     return res

    # def source_path(self, root):
    #     if not root: return 0
    #     stack = [(root,0)]
    #     res = float('-inf')
    #     while stack:
    #         node, parent_sum = stack.pop()
    #         _sum = parent_sum + node.val
    #         res = max(res, _sum)
    #         if node.right: stack.append((node.right, _sum))
    #         if node.left: stack.append((node.left, _sum))
    #     return res
# @lc code=end

