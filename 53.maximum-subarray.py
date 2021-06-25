#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=nums[0]
        m=[]
        m.append(sum)
        for i in nums[1:]:
            sum=max(i,sum+i)
            m.append(sum)
        return max(m)
        
# @lc code=end

