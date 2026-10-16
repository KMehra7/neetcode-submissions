class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                
        #Edge case if no input is provided
        if not grid or not grid[0]:
            return 0

        #Using BFS
        def bfs(r,c):
            q = deque([(r,c)])
            # visited.add((r,c))
            while q:
                #using row and col instead of r and c
                row, col = q.popleft()
                #using x and y in place of dr and dc
                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    newRow, newCol = row + x, col + y
                    # if newRow < 0 or newRow >= rows 
                    # or newCol < 0 or newCol >= cols
                    # or grid[newRow][newCol] == "0"
                    if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == "1" and (newRow, newCol) not in visited:
                        visited.add((newRow,newCol))
                        q.append((newRow,newCol))                
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    islands += 1
                    # dfs(r,c)
        
        return islands