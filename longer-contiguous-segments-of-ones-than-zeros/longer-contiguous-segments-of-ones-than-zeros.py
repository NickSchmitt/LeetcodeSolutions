class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        """
        - count consecutive ones and track high score
        
        - count consecutive zeroes and track high score
        
        - return high_ones > high_zeroes
        
        ---
        
        - count conseuctive ones and track high score
        - return high score
        """
        
        one_counter = 0
        one_high_score = 0
        
        zero_counter = 0
        zero_high_score = 0
        
        for i in s:
            if i == '1':
                one_counter += 1
                one_high_score = max(one_counter, one_high_score)
                zero_counter = 0
                
            if i == '0':
                zero_counter += 1
                zero_high_score = max(zero_counter, zero_high_score)
                one_counter = 0
                
        return one_high_score > zero_high_score