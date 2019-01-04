class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrow , ncol = len(grid), len(grid[0])
        
        for i in range(nrow):
            for j in range(ncol):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1] 
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[nrow-1][ncol-1]
