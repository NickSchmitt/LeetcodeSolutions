class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        left, right = 0, len(height)-1
        
        lmax, rmax = height[left], height[right]
        
        count = 0
        
        while left < right:
            
            if lmax < rmax:
                left+=1
                if height[left] > lmax: lmax = height[left]
                count += lmax - height[left]
            else:
                right-=1
                if height[right] > rmax: rmax = height[right]
                count += rmax - height[right]
                
        return count