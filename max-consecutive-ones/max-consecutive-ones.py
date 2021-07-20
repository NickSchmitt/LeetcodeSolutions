class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        
        
        """
        # keep track of a counter
        # keep track of high score
        
        # go over the list
            # if i encounter a 1, increment my counter
            
            # compare my counter to the highscore
            # and if my counter is greater, the highscore becomes what my counter is currently at
            
            
            # else if i encounter a 0
                # reset the counter
                
        # return our high score
        
        counter = 0
        high_score = 0
        
        for i in nums:
            if i == 1:
                counter += 1
                high_score = max(counter, high_score)
                
            else:
                #reset the counter
                counter = 0
                
        return high_score
                