class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        curr_combs = []
        
        def dfs(i):
            #Base case, current sum = target                
            if sum(curr_combs) == target:        
                combinations.append(curr_combs.copy())           
                return
            #Base Case, if i goes out of index or current sum > target
            if i >= len(nums) or sum(curr_combs) > target:
                return

            #Decision to add nums[i] and check
            curr_combs.append(nums[i])
            #first branch creation, adding same number
            dfs(i)
            #Pop the last nums[i] if we never use it
            curr_combs.pop()
            #add the next number, second branch decision
            dfs(i+1)

        dfs(0)
        return combinations

