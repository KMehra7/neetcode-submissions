class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #Idea is to start from first and last row and column
        #This ensures that those cells reach either one of the oceans
        #Since we start like this we will check for a greater value via DFS
        #if the height is greater then water can flow from edge to that cell
        res = []
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        
        #Use DFS
        def dfs(r, c, visited, prevHeight):
            if ((r,c)) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # Go through every single column in first row
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

