class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #Edge case
        #If substring length is more than actual string then ans is False
        if len(s1)>len(s2):
            return False
     
        #Array to keep track of counts of all a-z characters in both s1 and s2
        s1Count, s2Count = [0]*26, [0]*26

        #Update counts of every character in the range of our sliding window length
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        #Var set to 0 initially
        matches = 0

        #Creating inital matches at the start
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
            else:
                matches += 0
        
        #Sliding window portion
        l=0
        for r in range(len(s1),len(s2)):
            #If we already have 26 matches then return True else do the below operations to update 
            #Matches variable
            if matches == 26:
                return True
             
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches+=1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches+=1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l+=1
        return matches == 26
