class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph={}
        res=[]
        graph=self.buildGraph(equations, values, graph)
        for q in queries:
            
            res.append(self.bfs(q,graph))
        return res
                   
        
    def buildGraph(self,equation, value, graph):
        def add_edge(front, end, value):
            if front in graph:
                graph[front].append((end, value))
            else:
                graph[front]=[(end,value)]
        for vertices, value in zip(equation,value):
            print vertices,value
            front, end=vertices
            add_edge(front, end, value)
            add_edge(end, front, 1/value)
        return graph

    def bfs(self, query, graph):
            start,end=query
            if start not in graph or end not in graph:
                return -1.0
            queue=[(start, 1.0)]
            visited=set()
            while queue:
                start, product=queue.pop(0)
                if start==end:
                    return product
                visited.add(start)
                for neighbor, value in graph[start]:
                    if neighbor not in visited:
                        queue.append((neighbor, value*product))
            return -1.0
