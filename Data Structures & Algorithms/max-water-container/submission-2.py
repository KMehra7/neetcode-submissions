class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area=0
        for l in range(len(heights)):
            for r in range(l+1,len(heights)):
                currArea = (r-l) * min(heights[l],heights[r])
                # print(currArea)
                if currArea>=area:
                    area=currArea
        return area