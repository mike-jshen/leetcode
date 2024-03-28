
def longestSub(s: str) -> int:
    l = 0
    cur = {} # store character position in hash
    result = 0
    for c , v in enumerate(s):

        if v in cur:
            l = max(l,cur[v] + 1)

        cur[v] = c
        result = max(result , c - l)
    return result + 1
    
if __name__ == '__main__':
    string = "teststring"
    print(longestSub(string))
