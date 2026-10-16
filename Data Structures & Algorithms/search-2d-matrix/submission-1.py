class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #len(matrix) is no of rows present
        l,r = 0, len(matrix)-1
        while l<=r:
            m = (l+r)//2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                #we break out of this while loop in case our
                #target value falls in the current middle list
                break
        #If none of the lists contain the target val return False
        if not (l<=r):
            return False       
        #len(matrix[0]) is no of columns present i.e., 
        #no of elements in each list
        m = (l+r)//2
        low, high = 0, len(matrix[0])-1
        while low<=high:
            mid = (low+high)//2
            if matrix[m][mid] < target:
                low = mid + 1
            elif matrix[m][mid] > target:
                high = mid-1
            else:
                return True              
        return False
