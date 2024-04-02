class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        t = reversed(s)
        for c in t:
            if c == ' ' and result > 0:
                return result
            elif c != ' ':
                result += 1
        return result
