class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        countDict = {}
        counts = [ [] for i in range(len(nums) + 1) ]

        for n in nums:
            countDict[n] = 1 + countDict.get(n, 0)
        for n,c in countDict.items():
            counts[c].append(n)
        # print(counts)
        for i in range(len(counts) - 1, 0, -1):
            #Since list of lists we need to iterate through them
            #since most freq can be in one list itself
            for n in counts[i]:
                res.append(n)
                if len(res) == k:
                    return res
