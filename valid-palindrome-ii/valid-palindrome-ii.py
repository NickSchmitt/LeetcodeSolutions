class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        
        while left<right:
            if s[left]!=s[right]:
                return (s[left:right] == s[left:right][::-1] or         # checks from left to before right
                        s[left+1:right+1] == s[left+1:right+1][::-1]   # checks after left to right
                       )
            left+=1
            right-=1
        return True