class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        # base case
        dp[0][0]=1

        for i in range(1,m):
            dp[i][0]=dp[i-1][0] if obstacleGrid[i][0]==0 else 0
        for i in range(1,n):
            dp[0][i]=dp[0][i-1] if obstacleGrid[0][i]==0 else 0

        # recurrence
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]




if __name__=='__main__':
    A=Solution()
    result=A.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
    print result
