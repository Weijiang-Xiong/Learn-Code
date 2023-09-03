"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Solution:

At each step, the robot can either go right or go down. It needs (m-1) right and (n-1) down, and it can freely choose their order. 
So, it's the possible ways to choose m-1 elements from m+n-2 elements. 
math.comb(m+n-2, )

"""
class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        memory = [[-1 for _ in range(n)] for _ in range(m)]
        
        return num_unique(m, n, memory)
    
    def uniquePaths_math(self, m: int, n: int) -> int:
        import math
        return math.comb(m+n-2, m-1)

def num_unique(m, n, memory):
    
    if memory[m-1][n-1] > 0:
        return memory[m-1][n-1]
    
    if m == 1 or n == 1:
        res = 1
    else:
        res = num_unique(m-1, n, memory) + num_unique(m, n-1, memory)
    
    memory[m-1][n-1] = res
    
    return res
    

res = Solution().uniquePaths(5, 6)
print(res)