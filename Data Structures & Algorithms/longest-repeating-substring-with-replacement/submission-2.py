class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        countMap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            countMap[s[r]] = 1 + countMap.get(s[r],0)
            print('[s[r]]', [s[r]])
            print('countMap[s[r]]',countMap[s[r]])
            print('(r - l + 1) ',(r - l + 1) )
            print('max(countMap.values())', max(countMap.values()))
            if (r - l + 1) - max(countMap.values()) <= k:
                res = max(res, r-l+1)
                print('res', res)
            else:
                print('[s[l]]', [s[l]])
                print('countMap[s[l]]',countMap[s[l]])
                countMap[s[l]] -= 1
                l+=1
        return res