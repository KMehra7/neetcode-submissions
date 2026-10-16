class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # ans = []
        for i in range(len(nums)):
            print(i)
            print('nums[i]',nums[i])
            for j in range(i+1,len(nums)):
                print(j)
                print('nums[j]', nums[j])
                if nums[i]+nums[j]==target:
                    # ans.append(i)
                    # ans.append(j)
                    return(i,j)
        # return ans