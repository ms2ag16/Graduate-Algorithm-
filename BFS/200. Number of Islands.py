from collections import deque
class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """ using BFS, if the lands is connected, then merge all of them into 1"""
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.bfs(grid, i, j)
                    islands += 1
                    
        return islands  
    
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        que = deque()
        que.append((i, j))
        grid[i][j] = '0'
        while que:
            row, col = que.popleft()
            if row>0 and grid[row-1][col]=='1':
                que.append((row-1, col))
                grid[row-1][col] = '0'
            if row<m-1 and grid[row+1][col] == '1':
                que.append((row+1, col))
                grid[row+1][col] = '0'
            if col>0 and grid[row][col-1]=='1':
                que.append((row, col-1))
                grid[row][col-1] = '0'
            if col<n-1 and grid[row][col+1] == '1':
                que.append((row, col+1))
                grid[row][col+1] = '0'
