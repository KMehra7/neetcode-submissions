class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        res = 0

        for num in nums:
            if (num-1) not in numSet: #If not there, then no is starting point
                length = 1 #Initial length of seq is 1
                while (num+length) in numSet: #While next no exists increase length
                    length+=1
                res = max(res, length) #store max value found till now
        return res
            