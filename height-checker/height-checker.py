class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        difference = 0
        for (e, h) in zip(expected, heights):
            if e != h: difference+=1
        return difference
        
        # return sum([1 for h, s in zip(heights, sorted(heights)) if h!=s])