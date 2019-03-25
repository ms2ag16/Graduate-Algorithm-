"""
2D平面上，有m个人（P），n辆自行车(B)，还有空白（O）满足以下条件
1.m < n
2.不存在两个人，到同一辆自行车距离相等, 距离用abs(x1-x2) + abs(y1-y2)定义
3.每个人尽量找离自己最近的自行车，一旦某辆自行车被占，其他人只能找别的自行车。
例：
OPOBOOP
OOOOOOO
OOOOOOO
OOOOOOO
BOOBOOB
红色的人找到第一行的自行车，距离最近。
蓝色的人离第一行自行车最近，但自行车已经被红色人占有，所以他只能找离他第二近的，右下角的自行车。

问：把人和自行车配对，输出vector<pair<int, int>>每个人对应的自行车. {i, j} 是人i对应自行车j
"""

from heapq import heappop, heappush

class Solution(object):
    def findPairs(self, matrix):
        visited = set([])
        peoples = []
        bikes = []
        nrow, ncol = len(matrix), len(matrix[0])
        heap = []
        res = []

        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 'P':
                    peoples.append((i, j))
                if matrix[i][j] == 'B':
                    bikes.append((i, j))
        #print(bikes, peoples)

        for p in peoples:
            px, py = p
            for b in bikes:
                bx, by = b
                dist = abs(px - bx) + abs(py - by)
                heappush(heap, (dist, p, b))

        while heap:
            minDist, p, b = heappop(heap)
            if b not in visited and p not in visited:
                visited.add(b)
                visited.add(p)
                res.append((p,b))

        print (res)




if __name__ == "__main__":
    matrix = [ ['O', 'P', 'O', 'B', 'P', 'O', 'P'],
               ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
               ['B', 'O', 'O', 'B', 'O', 'O', 'B']]

    print Solution().findPairs(matrix)

