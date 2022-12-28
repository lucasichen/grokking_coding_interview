#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None: return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevel = 0
            num = 0
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel += currentNode.val
                num += 1
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
            res.append(currentLevel/num)
        return res
# @lc code=end

