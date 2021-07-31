from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = 0
        grouped = Counter(nums) if k == 0 else set(nums)
        
        if k==0:
            for num in grouped:
                if grouped[num] > 1:
                    count += 1
        
        else:
            for num in grouped:
                if num + k in grouped:
                    count += 1
                

        return count