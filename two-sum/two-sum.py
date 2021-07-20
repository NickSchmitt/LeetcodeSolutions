class Solution:
    def twoSum(self, nums, target):
        
        
        hash_map = {}
        
        for i, num in enumerate(nums):
            diff = hash_map.get(target-num)
            if diff:
                return [i, diff[0]]
            else: hash_map[num] = (i, num)