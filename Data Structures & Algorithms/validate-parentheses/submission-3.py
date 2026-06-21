class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if (c == ']' and prev != '[') or (c == '}' and prev != '{') or (c == ')' and prev != '('):
                    return False
        return len(stack) == 0
                

                