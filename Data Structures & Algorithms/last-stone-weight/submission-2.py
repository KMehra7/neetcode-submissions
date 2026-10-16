class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        if len(stones) == 1:
            return -1*stones[0]

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1==s2:
                if len(stones) == 0:
                    return 0
                else:
                    continue
            else:
                res_weight = abs( (-1*s1) - (-1*s2) )
                heapq.heappush(stones, -1*res_weight)
        return -1*stones[0]