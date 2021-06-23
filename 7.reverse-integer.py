#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sol=0
        if(x>=0):
            sign=1
        else:
            sign=-1
        x=abs(x)
        for i in range(len(str(x))):
            z=x%10
            sol=(sol*10)+z
            x=x//10
        if pow(-2,31) > sol*sign or pow(2,31) < sol*sign:
            return 0

        return sol*sign
        
# @lc code=end

