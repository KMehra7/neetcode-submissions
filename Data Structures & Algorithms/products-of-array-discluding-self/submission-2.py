class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #get prefix and postfix products
        prefix = []
        curr_prefix = 1
        for n in nums:
            prefix.append(curr_prefix)
            curr_prefix *= n
        print(prefix)

        postfix = [0] * len(nums)
        curr_postfix = 1
        for n in range(len(nums) - 1, -1, -1):
            # print(curr_postfix)
            postfix[n] = curr_postfix
            curr_postfix *= nums[n]
        print(postfix)
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res