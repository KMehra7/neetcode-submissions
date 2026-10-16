class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "+",
        }
        res = []

        def dfs(i, cur_str):

            if i == len(digits):
                res.append(cur_str)
                return
            for ch in digitToChar[digits[i]]:
                dfs(i+1, cur_str + ch)

        if digits: dfs(0, "")
        return res
