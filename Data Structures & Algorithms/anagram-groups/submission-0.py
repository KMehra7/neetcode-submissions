class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            # print(s)

            count = [0] * 26

            for ch in s:
                print(ch)
                count[ord(ch) - ord("a")] += 1
            # print(count)

            res[tuple(count)].append(s)

            # print(res)
            
        # print(res.keys())
        # print(res.values())
        return res.values()
        



