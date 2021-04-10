class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        max_three = set()
        
        for i in nums:
            # only adds if unique
            max_three.add(i)
            # if unique, remove fourth max
            if len(max_three) > 3: max_three.remove(min(max_three))
        # if at least 3 unique return third max
        if len(max_three) == 3: return min(max_three)
        # else return first max
        return max(max_three)