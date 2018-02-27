# dfs implement

class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

          # @param node, a undirected graph node
          
def cloneGraph(node):
        if not node:
            return node
        root=UndirectedGraphNode(node.label)
        stack=[node]
        visit={}
        visit[node.label]=root
        while stack:
            top=stack.pop()
            for n in top.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label]=UndirectedGraphNode(n.label)
                visit[top.label].neighbors.append(visit[n.label])

        return root
