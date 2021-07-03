#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if(len(height))<=1:
            return 0
        maxArea=0
        l=0
        r=len(height)-1
        while l<r:
            area=(min(height[l],height[r]))*(r-l)
            if(area>maxArea):
                maxArea=area
            if(height[r]>=height[l]):
                l+=1
            else:
                r-=1
        return maxArea

        
# @lc code=end

