class Solution:
    def validPalindrome(self, s: str, deleted=False) -> bool:
        
        if len(s) == 1: return True

        left=0
        right=len(s)-1
        
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                if not deleted: 
                    return self.validPalindrome(s[left:right], True) or self.validPalindrome(s[left+1:right+1], True)
                else:
                    return False
        return True