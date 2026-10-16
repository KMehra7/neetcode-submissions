class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            #If the same values come again we dont want to 
            #repeat the process for it so we skip it
            #and move on to the next one
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum < 0 :
                    l+=1
                elif cur_sum > 0:
                    r-=1
                else:
                    res.append([nums[i] , nums[l] , nums[r]])
                    l+=1
                    #To not have same sum we shift left pointer again
                    #We check if the previous and current left ptr numbers are same or not
                    #If they are and while l<r keep increasing l by 1
                    #This takes care of duplicate values
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res