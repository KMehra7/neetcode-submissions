class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = []
        for p,s in zip(position, speed):
            res.append((p,s))
        res.sort(reverse=True)
        # print(res)
        stack = []
        turns = 0
        for i in range(len(res)):
            # print(res[i][0])
            turns = (target-res[i][0])/res[i][1]
            if stack and turns <= stack[-1]:
                continue
            stack.append(turns)
        return len(stack)

