class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for each in tokens:
            if each == "+":
                stack.append(stack.pop() + stack.pop())
            elif each == "-":
                stack.append(stack.pop()*(-1) + stack.pop())
            elif each == "*":
                stack.append(stack.pop() * stack.pop())
            elif each == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(each))
        return stack[0]