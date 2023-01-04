#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# brute force method
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        stack = [root]
        while stack:
            loc = 0
            node = stack.pop()
            if node.left: 
                stack.append(node.left)
                loc += self.source_from_node(node.left)
            if node.right: 
                stack.append(node.right)
                loc += self.source_from_node(node.right)
            res = max(res, loc)
        return res

    def source_from_node(self, root):
        if not root: return 0
        dep = 0
        queue = deque()
        queue.append(root)
        while queue:
            level = len(queue)
            dep += 1
            for _ in range(level):
                currentNode = queue.popleft()
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
        return dep

# # efficent way
# class Solution:
#     # Efficent way
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         res = 0
#         def dfs(node):
#             nonlocal res
#             if not node: return -1
#             left = dfs(node.left)
#             right = dfs(node.right)
#             res = max(res, 2 + left + right)
#             return max(left, right) + 1
#         dfs(root)
#         return res
# @lc code=end

