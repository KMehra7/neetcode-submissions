class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # l,r = 0,len(nums)-1
        res=[]
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)):
            #If the same values comes again we dont want to repeat the process for it so skip
            #and move on to the next one
            if i>0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1,len(nums)-1
            while l<r:
                # print(nums[i] + nums[l] + nums[r])
                if nums[i] + nums[l] + nums[r] < 0 :
                    l+=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    #Consumes more memory so not using it
                    # if [nums[i],nums[l],nums[r]] not in res:
                    res.append([nums[i],nums[l],nums[r]])
                    #we update only left pointer since right pointer is updated above
                    l+=1 
                    #To not have same sum we shift left pointer again
                    #We check if the previous and current left ptr numbers are same or not
                    #If they are and while l<r keep increasing l by 1
                    #This takes care of duplicate values
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return res