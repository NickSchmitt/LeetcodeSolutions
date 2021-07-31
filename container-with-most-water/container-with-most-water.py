
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        186254837
        
        
        """
        i = 0
        j = len(height)-1
        
        ans = 0
        
        while i<j:
            x = j-i
            y = min(height[j], height[i])
            ans = max(x*y, ans)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return ans