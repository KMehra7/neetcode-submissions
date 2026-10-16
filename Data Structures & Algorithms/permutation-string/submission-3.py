class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2): return False
        #O(26.N) soln with Hashmap
        countMapS1 = {}
        countMapS2 = {}

        for i in range(len(s1)):
            countMapS1[s1[i]] = 1 + countMapS1.get(s1[i],0)
            # countMapS2[s2[i]] = 1 + countMapS2.get(s2[i],0)

        # if countMapS1 == countMapS2: return True
        
        l = 0
        for r in range(len(s2)):
            print('countMapS1',countMapS1)
            print('countMapS2',countMapS2)
            
            countMapS2[s2[r]] = 1 + countMapS2.get(s2[r],0)
            print('r-l+1',r-l+1)
            if r >= len(s1):
                print('countMapS2[s2[l]]',countMapS2[s2[l]])
                countMapS2[s2[l]] -= 1
                if countMapS2[s2[l]] == 0:
                    countMapS2.pop(s2[l])
                l+=1
            if countMapS1 == countMapS2: return True
            
        return False
        


        #O(N) solution 
        # s1Count, s2Count = [0]*26, [0]*26  
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord("a")] += 1
        #     s2Count[ord(s2[i]) - ord("a")] += 1
        # print('s1Count',s1Count)
        # print('s2Count',s2Count)
        # matches = 0

        # for i in range(26):
        #     if s1Count[i] == s2Count[i]:
        #         matches += 1
        #     else:
        #         matches += 0
        # print(matches)

        # l = 0
        # for r in range(len(s1),len(s2)):
        #     if matches == 26:
        #         return True
            
        #     index = ord(s2[r]) - ord("a")
        #     s2Count[index] += 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] + 1 == s2Count[index]:
        #         matches -= 1
            
        #     index = ord(s2[l]) - ord("a")
        #     s2Count[index] -= 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] - 1 == s2Count[index]:
        #         matches -= 1
        #     l+=1
        # return matches == 26
            
