#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            st = ""
            if i % 3 == 0 and i % 5 == 0: st = "FizzBuzz"
            elif i % 3 == 0: st = "Fizz"
            elif i % 5 == 0: st = "Buzz"
            else: st = str(i)
            res.append(st)
        return res

# @lc code=end

