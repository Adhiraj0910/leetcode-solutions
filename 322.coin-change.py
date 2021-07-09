#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if(coins[j]<=amount):
                    dp[i]=min(dp[i],1+dp[i-coins[j]])
        if(dp[amount]>amount):
            return -1
        else:
            return dp[amount]



        
# @lc code=end