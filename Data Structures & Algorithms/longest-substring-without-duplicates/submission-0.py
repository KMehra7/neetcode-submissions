class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        # To know if we have a duplicate or not we use set()
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            #We keep checking if there are any duplicates present
            #And keep removing them from the set and shift our starting point 
            #Of our input once to the right.
            #When we stop we have the next possible substring.
            #Get the length of it and compare it with the previous substring's length.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res