class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prdts = [1] * len(nums)
        prefix=1
        for i in range(len(nums)):
            print('prefix')
            print(prdts[i])
            print(prefix)
            prdts[i] = prefix
            print(prdts[i])
            prefix *= nums[i]
            print(prefix)
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            print('postfix')
            print(prdts[j])
            print(postfix)
            prdts[j] *= postfix
            postfix *= nums[j]
            print(prdts[j])
            print(postfix)
        return prdts
            
      
                
                
