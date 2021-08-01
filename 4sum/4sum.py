class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        return self.threeSum(nums, target, 4)
        
    def threeSum(self, nums, target, n):
        
        threeSums = []
        
        if len(nums) == 0 or nums[0] * n > target or target > nums[-1] * n:
            return threeSums
        
        if n == 2:
            return self.twoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in self.threeSum(nums[i + 1:], target-nums[i], n-1):
                    threeSums.append([nums[i]] + subset)
                    
        return threeSums

        
    def twoSum(self, nums, target):
        
        res = []
        left, right = 0, len(nums)-1
        
        while left < right:
            curr = nums[left] + nums[right]
            if curr < target or (left > 0 and nums[left] == nums[left-1]):
                left += 1
                
            elif curr > target or (right < len(nums) - 1 and nums[right] == nums[right+1]):
                right -= 1
                
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
        return res
            
        
"""
[1,0,-1,0,-2,2]
[-2, -1, 0, 1, 2]

-2: 
[]
"""