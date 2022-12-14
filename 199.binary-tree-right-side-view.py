#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return root
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = len(queue)
            for i in range(0,level):
                currentNode = queue.popleft()
                if i == level - 1: res.append(currentNode.val)  # if last node in level
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
        return res
# @lc code=end

