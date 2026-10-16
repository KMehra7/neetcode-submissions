class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        # Time Compl O(n * m * dfs()); 
        # time compl of dfs() is 4(no of times called) ^ length of word!
        
        #Use DFS concept for backtracking
        visited = set()
        #i is the current position of the word
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or
                word[i] != board[r][c] #if we found wrong ch we return False
                or (r,c) in visited) :
                return False
            visited.add((r,c))
            res = ( dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1))
            visited.remove((r,c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False
