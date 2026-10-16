class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        ans = False
        for i in nums:
            if i in temp:
                ans = True
            temp.append(i)
        return ans