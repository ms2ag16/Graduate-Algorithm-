# DAG Implementation
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
