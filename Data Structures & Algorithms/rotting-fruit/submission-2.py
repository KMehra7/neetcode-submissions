class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        mins = 0
        for r in range(rows):
            for c in range(cols):
                #Count fresh oranges initially
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh > 0 and q :
            #We pop every single rotten orange
            #at same time we add adjacent oranges to queue marking as rotten
            #thus we use for loop and not just while q
            for i in range(len(q)):
                row, col = q.popleft()
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    rr, cc = row + x, col + y
                    if (
                        rr in range(len(grid))
                        and cc in range(len(grid[0]))
                        and grid[rr][cc] == 1
                    ):
                        grid[rr][cc] = 2
                        q.append((rr,cc))
                        fresh -= 1
            mins+=1
        return mins if fresh == 0 else -1