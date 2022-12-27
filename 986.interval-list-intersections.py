#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j, start, end = 0, 0, 0, 1

        while i < len(firstList) and j < len(secondList):
            a_on_b = firstList[i][start] >= secondList[j][start] and firstList[i][start] <= secondList[j][end]
            b_on_a = secondList[j][start] >= firstList[i][start] and secondList[j][start] <= firstList[i][end]
            if(a_on_b or b_on_a):
                res.append(
                    [max(firstList[i][start],secondList[j][start]),
                    min(firstList[i][end],secondList[j][end])]
                    )
            if firstList[i][end] < secondList[j][end]: i += 1
            else: j += 1

        return res
# @lc code=end

