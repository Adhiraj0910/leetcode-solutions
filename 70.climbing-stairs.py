#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==0 or n==1 or n==2):
            return n
        ans=[0]*(n+1)
        ans[1]=1
        ans[2]=2
        for i in range(3,n+1):
            ans[i]=ans[i-1]+ans[i-2]
        return ans[-1]
        
# @lc code=end

