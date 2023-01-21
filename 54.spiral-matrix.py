#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == [[]] or matrix is None: return []
        top, left, bot, right = 0, 0, len(matrix)-1, len(matrix[0])-1
        res = []
        while left <= right and top <= bot:
            # move left
            for i in range(left,right+1): res.append(matrix[top][i])
            top += 1

            # move down
            for i in range(top,bot+1): res.append(matrix[i][right])
            right -= 1

            # move left
            if top <= bot:
                for i in range(right,left-1,-1): res.append(matrix[bot][i])
                bot -= 1

            # move up
            if left <= right:
                for i in range(bot,top-1,-1):res.append(matrix[i][left])
                left += 1
        return res
# @lc code=end

