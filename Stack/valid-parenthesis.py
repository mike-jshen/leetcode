class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        brackets = {'(': 0, ')' : 0, '[': 1, ']' : 1, '{': 2, '}' : 2}
        stack = []

        for c in s:
            if c in op:
                stack.append(c)
            else:
                if not stack:
                    return False
                if brackets[stack[-1]] != brackets[c]:
                    return False
                stack.pop()
                    
        return not stack
