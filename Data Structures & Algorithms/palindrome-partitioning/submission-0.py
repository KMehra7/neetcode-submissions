class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur_substrings = []
        visited = set()
        def dfs(i):
            if i >= len(s) :
                res.append(cur_substrings.copy())
                return
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    cur_substrings.append(s[i:j+1])
                    dfs(j+1)
                    cur_substrings.pop()
        dfs(0)
        return res

        dfs(0)
        return res

