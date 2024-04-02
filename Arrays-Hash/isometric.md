# Isometric Strings
https://leetcode.com/problems/isomorphic-strings

## Intuitive solution
The essense of isometric strings is that within each position of characters contain the same characters.
What that means is that if one character exists in more than one position in the first string, the second
string must have its own same characters in their respective positions.

```
i.e: egg and boo

The first character is distinct character in its string for both strings.
The second and third character are both the same within each string.

THUS: "egg" and "boo" are isometric.
```
## Hashmap Solution O(n)

Using hashmaps, we can compare string key value pairs to see if the appropriate overlap occurs within the strings.
For each character within the string, we will assign a keypair value.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/15786935-58b8-4dbc-9524-359735d3d74b)

In this case, we only have to loop through each string once which yeilds n+n complexity. This would further simplfy 
down to O(n) time complexity.

For each character we are iterating through, if the character DOES NOT EXIST within the hash, we add the character 
pairs.

```
            if a not in pair and b not in pair.values():
                pair[a] = b
```
If the character DOES EXIST, then we refer to the key pair value to see if it matches with the current iteration.
If they dont match, then we know that the string is not isometric as the character pairs would not match within the string.
```
            elif pair.get(a) != b:
                return False
```
When loop fully concludes, if each pair equals its corresponding pair, we ```return true```

Full code (Python):
```
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pair = {}

        for a, b in zip(s , t):
            if a not in pair and b not in pair.values():
                pair[a] = b

            elif pair.get(a) != b:
                return False
        return True
```
