class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        if not A: return 0
        
        l = 0
        
        for i in A:
            if A[l] != i:
                l+=1
                A[l] = i
        return l+1 