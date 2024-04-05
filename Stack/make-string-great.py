class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        result = ""
        for c in s:
            if len(stk) > 0 and c.isupper() and c.lower() == stk[-1]:
                stk.pop()
            elif len(stk) > 0 and c.islower() and c.upper() == stk[-1]:
                stk.pop()
            else:
                stk.append(c)
        for c in stk:
            result += c
        return result
