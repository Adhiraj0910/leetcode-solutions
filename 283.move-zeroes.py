#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==0):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        

        
# @lc code=end

