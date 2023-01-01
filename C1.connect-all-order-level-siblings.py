from collections import deque

# refer: https://www.educative.io/m/connect-all-siblings
class Solution:
    def populate_sibling_pointers(root):
        #TODO: Write - Your - Code
        if root is None: return root

        queue = deque()
        queue.append(root)
        previousNode = None
        while queue:
            level = len(queue)
            for _ in range(level):
                currentNode = queue.popleft()
                if previousNode: previousNode.next = currentNode
                previousNode = currentNode
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
        return root