class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return -1

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1" or (r,c) in visited:
                return
            visited.add((r,c))
            # islands += 1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        def bfs(r,c): #USE QUEUES
            q = deque([(r,c)])
            while q:
                row, col = q.popleft()
                directions = [ (1,0), (-1,0), (0,-1), (0,1) ]
                for x,y in directions:
                    newRow, newCol = row + x, col + y
                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                        visited.add((newRow,newCol))
                        q.append((newRow,newCol))
        
        islands = 0
        visited = set()            
        rows, cols = len(grid), len(grid[0])
       
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1 
                    # dfs(r,c)
                    visited.add((r,c))
                    bfs(r,c)
        return islands