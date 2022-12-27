#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1,len(intervals)):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]
            if interval_start <= end:       # overlapping, adjust the end
                end = max(end, interval_end)
            else:                           # not overlapping
                merged_intervals.append([start,end])
                start = interval_start
                end = interval_end
        merged_intervals.append([start,end])
        return merged_intervals
# @lc code=end

