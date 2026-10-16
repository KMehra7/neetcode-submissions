class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return -1
        
        islands = 0
        totalIslands = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1" or (r,c) in visited:
                return
            visited.add((r,c))
            # islands += 1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    totalIslands += 1 
                    dfs(r,c)
        return totalIslands