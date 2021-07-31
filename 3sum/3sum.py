class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        sort nums
        go through each num doing two_sum(num)
        if it's the same as last time, skip it since we've done two sum for that very number
        if we get above 0, just return what we've got so far        
        """
        nums.sort()
        ans = []
        
        for idx in range(len(nums)):
            
            if idx == 0 or nums[idx-1] != nums[idx]:
                self.twoSumII(idx, ans, nums)            
            
        return ans
                   
        
        
        
            
    def twoSumII(self, idx, ans, nums):
        """
        sorted two_sum(idx)
        
        target = 0-nums[idx]
        
        put pointers at n+1 and end
        if larger than target, bring in right
        if less than target, bring in left
        """       
        
        target = 0-nums[idx]
        
        left = idx+1
        right = len(nums)-1
        
        while left < right:
            currsum = nums[idx] + nums[left] + nums[right]
            if currsum < 0:
                left +=1
            elif currsum > 0:
                right-=1
            else:
                ans.append([nums[idx], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left+=1
                
        