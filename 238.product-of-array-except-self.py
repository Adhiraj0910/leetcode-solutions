#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        answer=[]
        for i in range(len(nums)):
            answer.append(pre)
            pre*=nums[i]
        for i in range((len(nums)-1),-1,-1):
            answer[i]*=post
            post*=nums[i]
        return(answer)
        
# @lc code=end

