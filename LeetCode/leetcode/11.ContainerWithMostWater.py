from lcutils import * 

class Solution:
    
    # https://leetcode.com/problems/container-with-most-water/
    
    def maxArea(self, height: List[int]) -> int:
        
        L, R, maxW, MaxArea = 0, len(height)-1, len(height)-1, 0
        
        # decrease the width (either left or right), see what we got 
        for w in range(maxW, 0, -1):
            if height[L] < height[R]:
                MaxArea = max(MaxArea, height[L]*w)
                L += 1 
            else:
                MaxArea = max(MaxArea, height[R]*w)
                R -= 1
                
        return MaxArea
    
height = [1,8,6,2,5,4,8,3,7]
MaxArea = Solution().maxArea(height)
print(MaxArea)