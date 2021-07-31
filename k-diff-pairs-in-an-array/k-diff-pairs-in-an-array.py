from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = 0
        k_zero = k == 0
        
        if k==0:
            freq_map = Counter(nums)
            for num in freq_map:
                if freq_map[num] > 1:
                    count += 1
        
        else:
            s = set(nums)
            for num in s:
                if num + k in s:
                    count += 1
                

        return count