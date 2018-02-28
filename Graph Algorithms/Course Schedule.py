# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

class Solution(object):
    def canFinish(self, n, edges):
        graph = {i:set() for i in range(n)}
        indeg = {i:0     for i in range(n)}
        for s, e in set(tuple(x) for x in edges):
            graph[s] |= {e}
            indeg[e] += 1
        queue  =  [i for i in range(n) if not indeg[i]]
        visits =  set(queue)
        for node in queue:
            for neigh in graph[node]:
                if neigh in visits:
                    return False
                indeg[neigh] -= 1
                if not indeg[neigh]:
                    visits.add(neigh)
                    queue += neigh,
        return len(visits) == n

if __name__=="__main__":
    courses=Solution()
    print courses.canFinish(2, [[1,0],[0,1]])
