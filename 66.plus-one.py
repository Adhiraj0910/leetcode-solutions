#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=0
        for i in range(len(digits)):
            result=(result*10)+digits[i]
        final=[]
        result+=1
        for j in str(result):
            final.append(j)
        return final

            
        
# @lc code=end

