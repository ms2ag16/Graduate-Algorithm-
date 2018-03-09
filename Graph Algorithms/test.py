    inlist={}
        outdegree={}

        for node in self.adjList.keys():
            if len(self.adjList[node])==0:
                self.adjList[node].append(node)

        for node in self.adjList.keys():
            for neighbor in self.adjList[node]: # loop node's neighbor, add node as inlist node pointing to each neighbor
                inlist.setdefault(neighbor,[]).append(node)
            # build out-degree structure
            outdegree.setdefault(node,[]).append(len(self.adjList[node]))


        sinkNodes=[]
        for node in self.adjList.keys():
            if len(self.adjList[node])==1 and (node in self.adjList[node]):
                sinkNodes.append(node)
            elif len(self.adjList[node])==0:
                sinkNodes.append(node)
