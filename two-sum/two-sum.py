class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        
        
        for i, num in enumerate(nums):
            if hash_map.get(target-num):
                return [i, hash_map.get(target-num)[0]]
            else: hash_map[num] = (i, num)
        
        # return "hello"