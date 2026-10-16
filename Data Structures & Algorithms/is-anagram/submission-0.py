class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s1 = list(s)
        t1 = list(t)
        # print(s1)
        # print(t1)
        s1_count = Counter(s1)
        t1_count = Counter(t1)

        s1_dict = dict(s1_count)
        t1_dict = dict(t1_count)

        print(s1_dict)
        print(t1_dict)

        if s1_dict == t1_dict:
            return True
        else: 
            return False