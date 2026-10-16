class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return -1
        
        checkDiff = {}

        for ind, el in enumerate(nums):
            diff = target - el
            if diff in checkDiff:
                return [checkDiff[diff], ind]
            checkDiff[el] = ind
        

        