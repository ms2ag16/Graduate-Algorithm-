"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
"""

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
