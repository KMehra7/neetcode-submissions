class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #Decision Trees
        #Sort the list cause we want all duplicate elements adjacent
        combinations = []
        curr_combination = []
        #Solution works only on sorted input
        candidates.sort()
        def dfs(i):
            if sum(curr_combination) == target:
                #create copy cause we pass curr_comb by reference
                combinations.append(curr_combination.copy())
                return
            if sum(curr_combination) > target or i == len(candidates):
                return
            
            #include candidates[i]
            curr_combination.append(candidates[i])
            dfs(i+1)
            curr_combination.pop()

            #skip candidates[i]
            #we use the while loop to skip same valued elements 
            #since we included them above
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return combinations