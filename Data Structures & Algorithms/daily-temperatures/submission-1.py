class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
 
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, ind]

        for i,t in enumerate(temperatures):
            # we check if our stack is not empty
            # then see if the present temp value is larger than
            # the one at the top of our stack, i.e., last appended
            while stack and t > stack[-1][0]:
                #If it is we pop the top of our stack
                stackT, stackInd = stack.pop()
                #We calculate the no of days by taking the diff
                #between ith index and ind of our top stack el
                #The corresponding ind value of temp is replaced by this diff
                res[stackInd] = (i - stackInd)
            #If current val isnt larger than top of stack, add that val to stack
            stack.append([t,i])
        return res