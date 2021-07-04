#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    romansDict = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}
    def romanToInt(self, s: str) -> int:
        currentVal=0
        final=0
        for i in s[::-1]:
            value=self.romansDict[i]
            if(value>=currentVal):
                final+=value
                currentVal=value
            else:
                final-=value
        return final
        
        
# @lc code=end

