#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda i:i[1])
        res = 1
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            if interval_start >= end:
                res += 1
                end = interval_end
        return len(intervals) - res
# @lc code=end

