class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        l,r = 0, 1
        maxProfit = 0

        while r<len(prices):
            if prices[l]<prices[r]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
            
    
        return maxProfit

        # minn = min(prices)
        # indMin = prices.index(minn)

        # if indMin == len(prices)-1:
        #     return 0

        # res = -minn
        # maxx = 0

        # for i in prices[indMin+1:]:
        #     maxx = max(maxx,i)
        
        # res += maxx

        # return res