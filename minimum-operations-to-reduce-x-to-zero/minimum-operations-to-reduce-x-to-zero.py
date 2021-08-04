from math import inf
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        
        total = sum(nums)
        target = total-x
        n = len(nums)
        
        maxi = -1
        left = 0
        current = 0
        
        for right in range(n):
            current += nums[right]
            while current > target and left <= right:
                current -= nums[left]
                left += 1
            
            if current == target:
                maxi = max(maxi, right-left+1)
        
        return n-maxi if maxi != -1 else -1
                