#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        originalNo = x
        sol=0
        if x<0:
            return False
        else:
            while x!=0:
                z=x%10
                sol=(sol*10)+z
                x=x//10
            if(sol==originalNo or originalNo==0):
                return True
        
# @lc code=end

