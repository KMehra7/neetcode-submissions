class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closedN):
            #Base case
            if openN == closedN == n:
                res.append("".join(stack))
                return
            #Add ( only if openN is less than n
            if openN < n:
                stack.append("(")
                #Backtrack recursively to add ( and increase count 
                #of openN by 1
                backtrack(openN + 1, closedN)
                #Update stack since we dont pass stack in every single call
                #It is a global variable
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        backtrack(0,0)
        return res        