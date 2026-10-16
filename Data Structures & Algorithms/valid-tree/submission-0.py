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
                if connectedEdge == prevNode:
                    continue
                if dfs(connectedEdge, i) == False:
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n

