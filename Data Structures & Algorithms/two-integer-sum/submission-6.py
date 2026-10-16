class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        
        for i in range(len(nums)):
            if target-nums[i] in tmp:
                return [tmp[target-nums[i]], i]
            tmp[nums[i]] = i