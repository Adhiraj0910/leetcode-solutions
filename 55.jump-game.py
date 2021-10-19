#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if (i+nums[i]>=reached):
                reached=i
        return reached==0
        
# @lc code=end

