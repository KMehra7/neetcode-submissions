class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = set(nums)
        longest=0

        for n in nums:
            if (n-1) not in res:
                length = 1
                while (n+length) in res:
                    length+=1
                longest = max(length,longest)
        return longest

        ''' Attempt 1
        nums = sorted(nums)

        print(nums)

        res=[]
        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                res.append(nums[i])
        print(res)
        ans=set()
        for i in range(len(res)-1):
            print(res[i],res[i+1])
            if res[i] + 1 == res[i+1]:
                ans.add(res[i])
                ans.add(res[i+1])

        print(ans)
        return len(ans) '''
