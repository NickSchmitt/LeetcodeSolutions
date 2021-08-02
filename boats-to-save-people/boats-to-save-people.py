class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        boats = 0
        
        left, right = 0, len(people)-1
        while right >= left:
            if people[left] + people[right] <= limit:
                left+=1
            boats += 1
            right -= 1
            
        print(boats)
        
        # boats += -(-(len(people[left:right+1])+1) // 2)
        
        return boats
            
            
            # if left and right can fit, increment boats and bring them both in
            # if not, increment boats
                
        """
        limit 5
        2,2,3,4,5,5
        ^left
              ^right
        boats 3
        2,2,3,4,6,6
          ^left
            ^right
        boats 
        
        2 6, bring in
        2 4 valid
        """