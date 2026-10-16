class Solution:
    def isValid(self, s: str) -> bool:
        
        hashMap = { '}':'{', ']':'[', ')':'('}
        stack=[]

        for i in s:
            if i in hashMap:
                if stack and stack[-1] == hashMap.get(i) :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack == []:
            return True
        else:
            return False