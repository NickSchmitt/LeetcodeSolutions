class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        
        window = len(needle)
        
        for i, x in enumerate(haystack):
            if needle == haystack[i:window+i]: 
                return i        
        return -1