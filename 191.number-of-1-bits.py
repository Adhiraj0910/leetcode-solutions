#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            x=int(math.log(n,2))
            n=n-pow(2,x)
            count+=1
            if(n==1):
                count+=1
                break
        return count

        
# @lc code=end

