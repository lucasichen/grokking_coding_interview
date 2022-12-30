#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return root
        queue = deque()
        queue.append(root)
        while queue:
            previousNode = None
            level = len(queue)
            for _ in range(level):
                currentNode = queue.popleft()
                if previousNode: previousNode.next = currentNode
                previousNode = currentNode
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
            
        return root
# @lc code=end

