class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount+1)
        # print(dp)
        dp[0] = 0
        # print(dp)

        for amt in range(1, amount + 1):
            for c in coins:
                # print('amt, c, amt - c', amt, c, amt - c)
                if amt - c >= 0:
                    # print('dp[amt] ', dp[amt] )
                    dp[amt] = min(dp[amt], 1 + dp[ amt - c])
                    # print('dp[amt] ', dp[amt] ) 
            # print(dp)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
        