class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        psum = 0
        
        for i, num in enumerate(nums):
            psum+=num
            nums[i] = psum
            
        return nums