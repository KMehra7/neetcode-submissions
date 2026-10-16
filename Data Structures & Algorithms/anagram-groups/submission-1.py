class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return ""

        groups = defaultdict(list)
        for s in strs:    
            #list to keep count of all lowercase letters 
            checkLetterCount = [0] * 26
            for ch in s:
                checkLetterCount[ord(ch) - ord("a")] += 1 
            groups[tuple(checkLetterCount)].append(s)
        
        return groups.values()