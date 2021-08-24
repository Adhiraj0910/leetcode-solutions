#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2=0,0

        for i in nums:
            rob=max(rob1+i,rob2)
            rob1=rob2
            rob2=rob
        return rob2
        
# @lc code=end

