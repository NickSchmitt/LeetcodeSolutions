class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        2,6,4,8,10,9,15
        
        2 15 valid
        2 6 9 15 valid
        2 6 4 10 9 15 invalid
        
        
        2,6,4,8,10,15
        
        bring things in until you find an invalid left and invalid right
        
        iterate that slice to find the min max
        push left back out until min < nums[left]
        push right back out until max > nums[right]
        
        
        """
        length = 0
        left = 0
        right = len(nums)-1
        
        while left < right and nums[left] <= nums[left+1]:
            left+=1
        
        if left == right: return 0
                
        while nums[right] >= nums[right-1]:
            if left == right: return 0
            right-=1
        
        unsorted = nums[left:right+1]
        unsorted_min, unsorted_max = min(unsorted), max(unsorted)
        
        
        while left > 0 and nums[left-1] > unsorted_min:
            left -= 1
            
        while right < len(nums)-1 and nums[right+1] < unsorted_max:
            right += 1
        
        print(nums[left])
        print(nums[right])
        print(nums[left:right+1])
        return len(nums[left:right+1])
        
        