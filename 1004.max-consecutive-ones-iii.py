#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# Need to redo
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start = 0
        max_length = 0
        max_ones = 0
        freq_map = {}

        for window_end in range(len(nums)):
            if nums[window_end] == 1:
                max_ones += 1

            if(window_end - window_start + 1 - max_ones) > k:
                if nums[window_start] == 1:
                    max_ones -= 1
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length
# @lc code=end

