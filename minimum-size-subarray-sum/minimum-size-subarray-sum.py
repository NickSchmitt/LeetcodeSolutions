from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        p1 = 0
        currsum = 0
        minsize = inf
        
        for p2, num in enumerate(nums):
            
            currsum += num
            while currsum >= target:
                minsize = min(minsize, p2-p1+1)
                currsum -= nums[p1]
                p1+=1
        
        return minsize if minsize != inf else 0
            