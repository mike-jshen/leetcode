class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        l = 1
        r = max(piles)
        k = math.floor((l+r)/2)

        while l < r:
            temp = 0
            for num in piles:
                temp += math.ceil(num/k)
            

            if temp <= h:
                r = k
                k = math.floor((r+l)/2)

            elif temp > h:
                l = k + 1
                k = math.floor((r+l)/2)

        return k
