class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = [] # (index, height) # Use index to calculate width

        for ind,height in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > height:
                index,h = stack.pop()
                maxArea = max(maxArea, h*(ind - index))
                start = index
            stack.append((start,height))

        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        
        return maxArea
            
        
            

