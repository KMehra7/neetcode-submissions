class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1 and nums[0]==target:
            return 0
        if nums == []:
            return -1

        low = 0
        high = len(nums)-1

        while low<=high:
            #In case of overflow which happens in Java/Javascript but not python
            #we can add the low val to the dist between high and low which we // by 2
            #   mid = low + ((high-low))//2)
            #high - low gives dist between them and halving the high ind
            #Avoids overflow
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
