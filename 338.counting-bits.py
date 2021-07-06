#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(n+1):
            count=0
            while i>0:
                x=int(math.log(i,2))
                i=i-pow(2,x)
                count+=1
            if(i==1):
                count+=1
            result.append(count)
        return result


        
# @lc code=end

