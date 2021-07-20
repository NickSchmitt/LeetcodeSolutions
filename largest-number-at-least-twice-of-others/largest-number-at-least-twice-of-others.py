class Solution:
    def dominantIndex(self, nums) -> int:
        
        largest = nums[0]
        largest = -1
        second_largest = -1
        result_index = -1
        
        for i, x in enumerate(nums):
            if x > largest:
                second_largest = largest
                largest = x
                result_index = i
            
            elif x > second_largest:
                second_largest = x
                
        if largest < second_largest*2:
            return -1
            
        return result_index
        