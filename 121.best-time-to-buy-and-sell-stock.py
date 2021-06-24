#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if(prices[i]<minimum):
                minimum=prices[i]
            else:
                profit=max(prices[i]-minimum,profit)
        return profit
# @lc code=end

