#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# Need to redo
# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart, max_length, max_repeat_char = 0, 0, 0
        freq_map = {}
        
        for windowEnd in range(len(s)):
            right_char = s[windowEnd]
            if right_char not in freq_map:
                freq_map[right_char] = 0
            freq_map[right_char] += 1
            max_repeat_char = max(max_repeat_char, freq_map[right_char])
        
            if(windowEnd - windowStart + 1 - max_repeat_char) > k:
                left_char = s[windowStart]
                freq_map[left_char] -= 1
                windowStart += 1

            max_length = max(max_length, windowEnd - windowStart + 1)
    
        return max_length

# @lc code=end

