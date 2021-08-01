class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.strip().split(" ")
        x = [word for word in x if word.isalnum()]
        left, right = 0, len(x)-1
        
        while left < right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -=1
        
        return " ".join(x)