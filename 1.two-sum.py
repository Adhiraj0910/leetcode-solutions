#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        listt=[]
        for i in range(len(nums)):
            for x in range(i+1,len(nums)):
                if(nums[x]+nums[i]==target):
                    listt.append(i)
                    listt.append(x)
                    return listt
# @lc code=end

