class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        #Enqueue all the gates (0s) initially since we traverse from them
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        #BFS from the gate
        while queue:
            r,c = queue.popleft()

            #Explore all 4 possible directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0, -1) ]:
                rr, cc = r + dr, c + dc

                #Continue if the new position is out of bounds
                #or is not an empty room
                if rr < 0 or rr >= rows or cc < 0 or cc >= cols or grid[rr][cc] != 2147483647:
                    continue
                
                #update the distance from the nearest gate
                grid[rr][cc] = grid[r][c] + 1

                #Enqueue the position
                queue.append((rr,cc))


'''
    class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #Initialize the queue
        q = deque()
        
        rows, cols = len(rooms), len(rooms[0])
        
        #Add all gates to queue so that we process them and their resp neighbours simultaneously
        for r in range(rows):
            for c in range(cols):
                #If it is a gate then add
                if rooms[r][c] == 0:
                    q.append((r,c))
        #BFS 
        while q:
            r, c = q.popleft()
            #Explore its neighbours in all 4 directions
            for dr, dc in [ (1,0), (-1,0), (0,-1), (0,1) ]:
                rr, cc = r + dr, c + dc
                
                #Check if either rr or cc is < 0 or if rr>=rows or if cc>=cols
                #or if value of cell rooms[rr][cc] != 2147483647
                #If any of the above condition are true then continue to next neighbour
                if rr < 0 or rr >= rows or cc < 0 or cc >= cols or rooms[rr][cc] != 2147483647:
                    continue
                
                #Update the distance in the queue
                #rooms[r][c] = 0 since we start from gate who's value is 0!!
                rooms[rr][cc] = rooms[r][c] + 1
                #Enqueue the neighbours to the queue to be processed next
                q.append((rr,cc)) 
'''