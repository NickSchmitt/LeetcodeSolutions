class Solution:
    def isHappy(self, n: int) -> bool:

        slow = n
        fast = self.sum_digit_squares(n)
        
        while slow!=fast:
            slow = self.sum_digit_squares(slow)
            fast = self.sum_digit_squares(self.sum_digit_squares(fast))
        return True if slow == 1 else False
            
    def sum_digit_squares(self, n):
        sum = 0
        while n > 0:
            n, d = divmod(n, 10)
            sum += d ** 2
        return sum
            
        
        