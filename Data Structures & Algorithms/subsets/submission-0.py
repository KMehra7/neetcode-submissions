class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        allSubsets = []
        subset = []
        #Think Decision Trees
        #Use DFS
        def dfs_to_getSubset(i):
            #Base Case for BackTracking
            #If current number index is out of bounds
            #Meaning we have reached our leaf node or we are at base
            if i >= len(nums):
                #Add copy of subset since subset gets modified
                #It is global so after loop it becomes empty
                allSubsets.append(subset.copy())
                return 

            #Decision to add the number nums[i]
            subset.append(nums[i])
            #recursive call
            dfs_to_getSubset(i+1)
            #backtrack by removing elements
            #Decision to not include nums[i]
            subset.pop()
            #Recursive call again since this has empty subset
            dfs_to_getSubset(i+1)

        dfs_to_getSubset(0)
        return allSubsets


''' include indv ele or not
    initially, all elements are not included
    before recursoin

    for loop for every element,
    1st line is to include the ele in set or turn it into 1 from 0
    '''