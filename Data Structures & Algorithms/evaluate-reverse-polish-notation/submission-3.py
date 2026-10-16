class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        num1,num2=0,0
        for token in tokens:
            if token == "+":
                add = stack.pop()+stack.pop()
                print("pushing add", add)
                stack.append(add)
            elif token == '-':
                a,b = stack.pop(), stack.pop()
                sub = b-a
                print("pushing sub", sub)
                stack.append(sub)
            elif token == '*':
                mul = stack.pop() * stack.pop()
                print("pushing mul", mul)
                stack.append(mul)
            elif token == '/':
                a,b = stack.pop(), stack.pop()
                div = int(float(b)/a)
                print("pushing div", div)
                stack.append(div)
            else:
                stack.append(int(token))
            
            print(stack)
        return stack[0]