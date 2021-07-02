#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        final=set()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            target=0-nums[i]
            while left<right:
                if(nums[left]+nums[right]==target):
                    final.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target :
                    left+=1
                else:
                    right-=1
        return list(final)

# @lc code=end

