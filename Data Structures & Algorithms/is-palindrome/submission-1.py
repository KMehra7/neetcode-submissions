class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ans=''
        for ch in s:
            if ch.isalnum():
                ans+=ch  
        ans=ans.lower()
        s1 = ans[:len(ans)//2]
        s2 = ans[len(ans)//2:]

        print(s1)
        print(s2)    

        length=0
        for c1,c2 in zip(s1,s2[::-1]):
            print(c1)
            print(c2)
            if c1==c2:
                length+=1
        
        if length==len(s1):
            return True
        else: 
            return False