class Solution:
    def climbStairs(self, n: int, cache={}) -> int:
        
        if n <= 2:
            return n
        
        if n in cache: 
            return cache[n]
        
        else:
            cache[n] = self.climbStairs(n-1, cache) + self.climbStairs(n-2, cache)
        
        return cache[n]