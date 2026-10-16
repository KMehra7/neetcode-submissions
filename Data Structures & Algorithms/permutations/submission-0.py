class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time O ( n! * n^2)
        # Space O (n! * n)


        #Iteratively
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms

'''
        #Recrusively simplified
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
'''            

'''
        #With Recursion
        #Base Case
        if len(nums) == 0:
            return [[]]
        #Keep calling recursive function with input nums without the first element
        #that is the subproblem
        #perms stores all the subproblems
        perms = self.permute(nums[1:])
        #then we want to add from these add the curr element that is at index 0
        # in every possible pos
        #store them in all_perms which we return
        all_perms = []
        #Go through every single perm we have
        for p in perms:
            #for each perm, go through every possible index that we can insert the current value into that perm
            #We add 1 to range since we can add curr num to the end of the perm
            for i in range(len(p)+1):
                #for that perm p
                #create a copy of it, cause we use it multiple times
                #dont want to modify the original
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                all_perms.append(p_copy)
        return all_perms
'''