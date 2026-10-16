class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1
        for n in nums:
            #Not necessary
            # if n == 0:
            #     curMin, curMax = 1, 1
            #     continue
            print('curMax', curMax)
            print('curMin', curMin)
            tmp = curMax * n
            print('tmp', tmp)
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)
            print('res', res)

        return res
            
