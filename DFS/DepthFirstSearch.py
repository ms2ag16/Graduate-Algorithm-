""" recursive logic"""
""" 
递归结束条件：节点是None，结束函数调用
递归改变：每次都要把节点添加到节点集合当中去
递归调用：对于每一个当前节点的相邻节点，只要不在节点集合中，就调用dfs进行搜索 
"""
def iterDFS():
    stack=[]
    visited=set()
    stack.append(self.root)
    visited.add(self.root)
    while stack:
        node=stack.pop()
        visited.add(node)
        do_proccess(node)
        neighbors=generated_unvisited_neighbors(node, visited)
        stack.extend(neighbors)
        
    
        
        


