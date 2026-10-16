class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time O(N+klogN) Space O(N)
        # maxheap = [ -num for num in nums]
        # heapq.heapify(maxheap)
        # i = 0
        # while i < k:
        #     curr = heapq.heappop(maxheap)
        #     i+=1
        # return -1*curr

        #Time O(NlogK) Space O(K)
        minheap = nums
        heapq.heapify(minheap)
        while len(minheap) > k:
            heapq.heappop(minheap)
        
        return minheap[0]
