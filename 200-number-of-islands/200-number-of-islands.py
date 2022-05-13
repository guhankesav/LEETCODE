class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows , cols = len(grid) , len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            
            queue = collections.deque()
            queue.append((r,c))
            
            while queue:
                row, col = queue.pop()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for i,j in directions:
                    r,c = row + i , col + j
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                        visited.add((r,c))
                        bfs(r,c)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    
                    bfs(r,c)
                    visited.add((r,c))
                    islands+=1
        
        return islands