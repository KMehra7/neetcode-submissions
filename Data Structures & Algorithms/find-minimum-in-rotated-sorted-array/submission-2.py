class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r = 0, len(nums)-1
        curr_min = 100000000
        while l <= r:    
            #If we are in a sorted array then compare l and r nums values
            #Get the curr_min by comaparing its current value with left most element
            #break out of the loop since we have checked other elements till now
            if nums[l] < nums[r]:
                curr_min = min(curr_min, nums[l])
                break
            #Perform Binary Search to keep finding the current min 
            m = (l+r)//2
            curr_min = min(curr_min, nums[m])
            #If middle element is greater than or equal to the left most element
            #then it is a part of the left sorted portion. Thus check right portion
            #left most value will always be the smallest in each portion
            if nums[m] >= nums[l]:
                l = m + 1
            #If it is not then check left portion. We check in left portion because all values
            #to the right of the right pointer will be greater than the current middle value
            else:
                r = m - 1
        return curr_min