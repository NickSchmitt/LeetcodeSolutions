from math import inf
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        """
        sort nums
        if num is same as last time, skip
        (don't do the "more than num break" rule because we're going for closest not exact)
        
        else do two_sum
        
        """
        diff = inf
        nums.sort()
        
        for idx in range(len(nums)):
            left, right = idx+1, len(nums)-1
            
            while left < right:
                currsum = nums[idx] + nums[left] + nums[right]
                if target == currsum: return target
                if abs(target-currsum) < abs(diff):
                    diff = target-currsum
                
                if currsum < target:
                    left+=1
                    
                else: right -= 1
                    
            if diff == 0: break
        return target-diff
        
            
        
        