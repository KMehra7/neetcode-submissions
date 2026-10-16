class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #For a Valid Tree
        #All nodes need to be connected without any loops/cycles
        #If length of visit set == n then Valid

        #Empty graph is a valid tree
        if not n:
            return True
        
        #Create Adjaceny list for all nodes
        edgeMap = { i:[] for i in range(n)}
        #Since undirected we add for both nodes
        for node1,node2 in edges:
            edgeMap[node1].append(node2)
            edgeMap[node2].append(node1)
        print(edgeMap)
        visit = set()
        def dfs(i, prevNode):
            
            #If cycle is present return False
            if i in visit:
                return False
            visit.add(i)
            for connectedEdge in edgeMap[i]:
                print(prevNode,i,connectedEdge)
                #Remember this, if the value of current connectedEdge is equal to
                #the prevNode then we move ahead
                #eg 1,4,1 -> if we are at node 4 its prev is node 1 and from adjList
                #its connectedEdges is 1 again, since we came from 1 we will not visit again
                #therefore skip this and continue to next connected edge
                if connectedEdge == prevNode:
                    continue
                if dfs(connectedEdge, i) == False:
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n

