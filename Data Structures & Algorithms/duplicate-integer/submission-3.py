class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) > pow(10,5):
            return False
        count = 0
        for i in range(len(nums)):
            print(i)
            print('nums[i]', nums[i])
            for j in nums[i+1:]:
                print('nums of j',j)
                if j== nums[i]:
                    count+=1

        if count >= 1:
            return True
        else:
            return False       
