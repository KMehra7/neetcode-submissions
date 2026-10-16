class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        starts = defaultdict(list)
        longest = 0
        for i in numSet:
            lst = []
            if i - 1 not in numSet:
                length = 1
                lst.append(i)
                while i + length in numSet:
                    lst.append(i+length)
                    length+=1
                starts[length].append(lst)
                longest = max(longest, length)
        # print(longest)
        # print(starts[4])
        print(starts[max(starts.keys())])
        return max(starts.keys())