from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        chars = Counter()
        i = j = longest = 0
        while j < len(s):
            chars[s[j]] += 1
            if j - i + 1 - max(chars.values()) > k:
                chars[s[i]] -= 1
                i+=1
            longest = max(longest, j-i+1)
            j+=1
        
        return longest