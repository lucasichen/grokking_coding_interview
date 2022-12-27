#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) + 1 == 1: return [newInterval]

        merged_intervals = []
        intervals.append(newInterval) # add new interval into intervals list
        intervals.sort(key=lambda i: i[0])
        start,end = intervals[0][0], intervals[0][1]

        for i in range(1,len(intervals)):
            interval_start = intervals[i][0]
            interval_end = intervals[i][1]

            if interval_start <= end:
                end = max(end, interval_end)
            else:
                merged_intervals.append([start,end])
                start = interval_start
                end = interval_end
        merged_intervals.append([start,end])
        return merged_intervals
# @lc code=end

