from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rowLen = len(grid)
        colLen = len(grid[0])
        
        dq = deque()
        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 2:
                    dq.append([i,j])
                    
        minutes = 0
        
        while(len(dq)>0):
            
            for _ in range(len(dq)):
                curr = dq.popleft()
                r = curr[0]
                c = curr[1]
                for x, y in directions:
                    if (
                        r+x > rowLen-1  or
                        r+x < 0         or
                        c+y > colLen-1  or
                        c+y < 0
                    ): continue
                        
                    if grid[r+x][c+y] == 1:
                        grid[r+x][c+y] = 2
                        dq.append([r+x, c+y])
            if len(dq)>0:    
                minutes+=1
        
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    return -1
        
        return minutes

    
"""
minutes start at 0

edge cases:

theres only 1 rotten orange, surrounded by empty cells
    answer should be 0

there's only empty cells
    answer should be 0
"""

            