class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check = {}
        for ind,num in enumerate(nums):
            diff = target - num
            if diff in check:
                return [check[diff], ind]
            check[num] = ind