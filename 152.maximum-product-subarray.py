#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax=1
        curMin=1
        for i in nums:
            temp=curMax
            curMax=max(i*curMax,i*curMin,i)
            curMin=min(i*temp,i*curMin,i)
            res=max(res,curMax,curMin)
        return(res)
        
# @lc code=end

