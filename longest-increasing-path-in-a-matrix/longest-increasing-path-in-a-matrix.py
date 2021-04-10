class Solution:
    def longestIncreasingPath(self, M: List[List[int]]) -> int:
        
        ylength = len(M)
        xlength = len(M[0])
        
        @cache
        def search_path(y, x):
            val = M[y][x]
            # returns the longest path of any adjacent value. Minimum will be itself (1 + max(0))
            return 1 + max(
                # search all adjacent values that are smaller than the current value.
                search_path(y+1,x) if y < ylength - 1 and val > M[y+1][x] else 0,
                search_path(y-1,x) if y > 0 and val > M[y-1][x] else 0, 
                search_path(y,x+1) if x < xlength - 1 and val > M[y][x+1] else 0,
                search_path(y,x-1) if x > 0 and val > M[y][x-1] else 0)
        
        # search path for all x and y, then return the max value
        return max(search_path(y, x) for y in range(ylength) for x in range(xlength))