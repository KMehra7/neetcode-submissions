class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Use 1 array only keeping memoryy in mind
        prdts = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            prdts[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            prdts[i] *= postfix
            postfix *= nums[i]
        return prdts

        #Using 2 arrays so memory used is more
        '''
        #get prefix and postfix products
        prefix = []
        curr_prefix = 1
        for n in nums:
            prefix.append(curr_prefix)
            curr_prefix *= n
        postfix = [0] * len(nums)
        curr_postfix = 1
        for n in range(len(nums) - 1, -1, -1):
            postfix[n] = curr_postfix
            curr_postfix *= nums[n]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res
        '''