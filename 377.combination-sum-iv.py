#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(targetCurr):
            sum=0
            if targetCurr==0:
                return 1
            elif targetCurr<0:
                return 0
            if targetCurr in memo:
                return memo[targetCurr]
            for i in nums:
                if targetCurr>=i:
                    sum+=dfs(targetCurr-i)
            memo[targetCurr]=sum
            return sum
        return dfs(targetCurr=target)



        
# @lc code=end

