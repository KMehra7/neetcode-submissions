class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Create a hashmap tp store nums as Keys and their index as values
        #Check if target-key is present in the hashmap
        #If not iterate and go to next num
        #If it is then return the indices then

        previous_map = {}

        for index,element in enumerate(nums):
            diff = target - element
            print('Before check hashmap', previous_map)
            if diff in previous_map:
                return [previous_map[diff], index]
            previous_map[element] = index
            print('After check and adding hashmap', previous_map)

        # Brute Force, O(n2)
        # for i in range(len(nums)):
        #     # print(i)
        #     # print('nums[i]',nums[i])
        #     for j in range(i+1,len(nums)):
        #         # print(j)
        #         # print('nums[j]', nums[j])
        #         if nums[i]+nums[j]==target:
        #             return(i,j)
        