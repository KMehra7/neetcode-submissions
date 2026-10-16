class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxheap = [ -num for num in nums]
        heapq.heapify(maxheap)
        i = 0
        while i < k:
            curr = heapq.heappop(maxheap)
            i+=1
        return -1*curr
