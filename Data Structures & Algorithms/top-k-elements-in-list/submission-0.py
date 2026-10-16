class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [ [] for i in range(len(nums) + 1)]        

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # print(count)
        # {1: 1, 2: 2, 3: 3}

        for n,c in count.items():
            freq[c].append(n)

        # print(freq)
        # [[], [1], [2], [3], [], [], []]

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # print(res)
                # [3]
                # [3, 2]
                # [3, 2, 1]
                
                # If res.append(freq[i]) is done without for n in freq[i]:
                # Then the res array will ook like this. We dont want empty ones
                # So we do it above to get just the non empty elements
                # []
                # [, ]
                # [, , ]
                # [, , , [3]]
                # [, , , [3], [2]]
                # [, , , [3], [2], [1]]
                if len(res)==k:
                    return res
                
