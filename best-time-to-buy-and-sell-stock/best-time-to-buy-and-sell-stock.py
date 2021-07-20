class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # going along, find the lowest price
        
        # if we find the lowest price, then find 
        
        least = 10e4+1
        max_profit = 0
        for i in prices:
            if i < least:
                least = i
            if i-least > max_profit:
                max_profit = i-least
        return max_profit
                
                
            