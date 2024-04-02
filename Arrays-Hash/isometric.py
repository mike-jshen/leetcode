class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}

        for a, b in zip(s , t):
            if a not in pair and b not in pair.values():
                pair[a] = b

            elif pair.get(a) != b:
                return False
        return True
