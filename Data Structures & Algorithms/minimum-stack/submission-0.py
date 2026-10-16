class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #We have another stack called MinStack to keep track of the min ele at that point 
        #We check current el with last el inserted in MinStack, whichever is smaller we insert that
        #into minstack thereby making it the min el.
        if self.minStack:
            val = min(val, self.minStack[-1])   
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
