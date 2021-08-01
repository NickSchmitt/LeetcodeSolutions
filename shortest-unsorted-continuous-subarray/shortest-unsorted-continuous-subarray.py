class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        length = 0
        left = 0
        right = len(nums)-1
        
        while left < right and nums[left] <= nums[left+1]:
            left+=1
                
        while nums[right] >= nums[right-1]:
            if left == right: return 0
            right-=1
        
        unsorted_min, unsorted_max = min(nums[left:right+1]), max(nums[left:right+1])
        
        
        while left > 0 and nums[left-1] > unsorted_min:
            left -= 1
            
        while right < len(nums)-1 and nums[right+1] < unsorted_max:
            right += 1
        
        return len(nums[left:right+1])
        
        