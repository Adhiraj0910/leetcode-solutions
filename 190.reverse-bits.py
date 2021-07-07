#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        originalNumber = '{0:032b}'.format(n)
        answer = originalNumber[::-1]
        return int(answer,2)
        
# @lc code=end

