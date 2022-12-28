#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        queue = deque()
        queue.append(root)
        dep = 0
        while queue:
            levelSize = len(queue)
            dep += 1
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
        return dep
# @lc code=end

