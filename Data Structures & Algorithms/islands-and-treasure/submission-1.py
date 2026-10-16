class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid:
            return None
        
        rows, cols = len(grid), len(grid[0])

        #BFS
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c)) #Start from treasure chests and traverse simultaneously
        while q:
            row, col = q.popleft()
            for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                rr, cc = row + x, col + y
                if rr < 0 or rr >= rows or cc < 0 or cc >= cols or grid[rr][cc] != 2147483647:
                    continue
                grid[rr][cc] = grid[row][col] + 1
                q.append((rr,cc))
        