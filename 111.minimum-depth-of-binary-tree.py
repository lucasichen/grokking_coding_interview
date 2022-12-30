#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        res = 0
        queue = deque()
        queue.append(root)
        while queue:
            level = len(queue)
            res += 1
            for _ in range(level):
                currentNode = queue.popleft()
                if currentNode.left == None and currentNode.right == None: return res
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
        return res
# @lc code=end

