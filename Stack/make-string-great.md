# Make The String Great
https://leetcode.com/problems/make-the-string-great
```
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
```

## Use Stack:
Like the valid parenthisis problem, we would append to a stack and check to see if the top letter within the stack is opposite 
in case and equal in character.

```Python
            if len(stk) > 0 and c.isupper() and c.lower() == stk[-1]:
                stk.pop()
            elif len(stk) > 0 and c.islower() and c.upper() == stk[-1]:
                stk.pop()
```

![image](https://github.com/mike-jshen/leetcode/assets/68671792/2924dc98-1c38-491e-8031-99e56a2a0d16)

## Inperfect substrings
The image above shows the logic that we are going for. In this case, both the "a" and "A" are not 
beside each other, but removing the substring "bB" gives us "aAcC" which in turn will give us 
the inperfect string. A stack will account for this sort of gap.

## Final String
If there are a series of lower/upper case letters that are different, then the characters should
remain the same.

```
str = "leEetcode"
str` = "leetcode"
```

We can see that in the "leEetcode" example, the only imperfect art is the "eE" and thus the stack 
will only remove the substring and keep everything else within it.

```Python
            else:
                stk.append(c)
```

The resulting stack is the string that we want.
```python
        for c in stk:
            result += c
        return result
```
## Runtime
Typically this would yeild a worst case runtime of O(n+n) if no characters need to be removed which
simplifies to O(n). The first loop would be looping through the string itself and the second would
be string parsing to loop through the stack.

## Code
```python
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
```
