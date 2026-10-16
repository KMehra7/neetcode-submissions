class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Logic
        #Create a dict with num:count pait
        #reverse it, for all the highest values add them to []
        #Bucket Sort, Time O(n), Space O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res