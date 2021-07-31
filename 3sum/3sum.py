class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # since our search is going to be the whole array for each elem (n^2) we can afford the nlogn sort
        ans = []
        
        for idx in range(len(nums)):
            if nums[idx] > 0: break                     # if num is above 0, we can't sum with new numbers to 0, so break
            if idx == 0 or nums[idx-1] != nums[idx]:    # perform two sum only if not duplicate
                self.twoSumII(idx, ans, nums)            
            
        return ans
        
            
    def twoSumII(self, idx, ans, nums):
        
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
                while left < right and nums[right] == nums[right+1]: # bring in either right or left to avoid duplicates
                    right-=1
                
        