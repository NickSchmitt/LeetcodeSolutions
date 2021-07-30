class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        
        left_idx = 0
        
        for i in nums:
            if nums[left_idx] != i:
                left_idx+=1
                nums[left_idx] = i
        num_unique = left_idx+1
        return num_unique  