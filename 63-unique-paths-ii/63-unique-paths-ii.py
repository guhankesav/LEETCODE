class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range (len(obstacleGrid)):
            for j in range (len(obstacleGrid[i])):
                if(i==0 and j==0):
                    if(obstacleGrid[i][j]==0):
                        obstacleGrid[i][j]=1
                    else:
                        obstacleGrid[i][j]=0                
                elif(i>0 and j>0):
                    if(obstacleGrid[i][j]==1):
                        obstacleGrid[i][j]=0
                    else:
                        obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                elif(i==0):
                    if(obstacleGrid[i][j]==0):
                        obstacleGrid[i][j]=obstacleGrid[i][j-1]
                    else:
                        obstacleGrid[i][j]=0
                elif(j==0):
                    if(obstacleGrid[i][j]==0):
                        obstacleGrid[i][j]=obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j]=0
        return obstacleGrid[-1][-1]