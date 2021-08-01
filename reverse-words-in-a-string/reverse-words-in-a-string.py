class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = [word for word in s.strip().split(" ") if word.isalnum()]
        
        left, right = 0, len(words)-1
        
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -=1
        
        return " ".join(words)