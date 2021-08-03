from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = defaultdict(int)
        
        p1 = longest = 0
        longest = 0
        
        for p2, char in enumerate(s):
            chars[char] += 1
            while chars[char] > 1:
                chars[s[p1]] -=1
                p1+=1
            
            longest = max(longest, p2-p1+1)
        
        return longest