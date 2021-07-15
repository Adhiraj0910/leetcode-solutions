#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        x=len(matrix)
        for i in range(x-1):
            for j in range(i+1,x):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(x):
            for j in range(x//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][x-1-j]
                matrix[i][x-1-j]=temp
        

        
# @lc code=end

