class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        
        for i in nums:
            if i != nums[left]:
                left+=1
                nums[left] = i
        
        return left+1
    
    