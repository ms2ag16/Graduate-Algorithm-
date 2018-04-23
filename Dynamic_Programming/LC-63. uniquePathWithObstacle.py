class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n,dp=len(obstacleGrid),len(obstacleGrid[0]),[0,1]
        dp+=[0]*(n-1)
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                dp[j]=(not obstacleGrid[i-1][j-1])* (dp[j]+dp[j-1])
        return dp[-1]


if __name__=='__main__':
    A=Solution()
    result=A.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
    print result
