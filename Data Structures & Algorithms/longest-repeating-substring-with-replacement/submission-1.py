class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        l = 0
        countMap = {}
        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r],0)

            if r-l+1 - max(countMap.values()) <= k:
                res = max(res, r-l+1)
                r+=1
            else:    
                countMap[s[l]] -= 1
                l+=1
        
        return res
        