class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m==1 and n==1:#edge case
            return 0
        if k >= n+m-3:#when this happen, promises that it can definitely reach bottom right
            return m+n-2
        queue = []
        steps = 0
        #visited:
        #to store the usage of elimination, if visited a same point with less elimination, then it could be considered as a possible solution
        visited = [[float('inf') for _ in range(n)] for _ in range(m)]
        queue.append((0, 0, 0))#(0, 0, 0) == (start_i, start_j, elimination usage)
        
        while queue:
            #every queue only stores path using same steps, don't have to store a steps with (i, j, obs) records
            newqueue = []
            for x, y, obs in queue:
                for i, j in (x+1, y), (x, y+1), (x-1, y), (x, y-1):
                    if 0<=i<m and 0<=j<n:#if the i, j are valid
                        if grid[i][j]==1:#there's a obstable, should use elimination
                            #traverse only if the obs usage is less than last time
                            #otherwise the steps is more and obs is more too, then no point to try
                            if visited[i][j] > obs+1 <= k:
                                visited[i][j] = obs+1
                                newqueue.append((i, j, obs+1))
                        else:#grid[i][j]==0
                            if i==m-1 and j==n-1:#hit the bottom right,which is possible only when grid[i][j]==0
                                return steps+1
                            #not yet bottom right
                            if visited[i][j] > obs:#traverse only when elimination usage is less than last time
                                visited[i][j] = obs
                                newqueue.append((i, j, obs))
            queue = newqueue
            steps += 1
        return -1