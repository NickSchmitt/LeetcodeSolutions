# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n
        while(left<right):
            mid = left + (right-left) // 2
            if isBadVersion(mid)==True:
                right = mid
            else:
                left = mid+1
        return left
        
        