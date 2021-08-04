class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        naive way:
        
        sort it, then iterate by two until we find two that aren't next to each other O(n log n)
        
        
        
        """
        
        ans = nums[0]
        
        for num in range(1, len(nums)):
            ans^=nums[num]
        
        return ans