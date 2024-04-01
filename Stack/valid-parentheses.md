## Valid Parenthesis
https://leetcode.com/problems/valid-parentheses/

## Intuitive Solution:
My first thought was to keep a counter for each parenthesis type. When there was an open bracket, we increase the counter
and when there is a close bracket, we decrease the counter. If all counters were to equal 0, we can assume that
parenthesis pairs exist.

HOWEVER, this solution would not work for the example ```")("``` since there is a pair that exists, the parenthesis
is not closed.

## Hash Classifier

First, we would want to group each pairs of parenthesis into a hash with its corresponding open and closed state.
```
        brackets = {'(': 0, ')' : 0, '[': 1, ']' : 1, '{': 2, '}' : 2}
```
This would ensure that when comparing for the open and closed brackets, we would only need to check if the values for
each parenthesis match. This would be a much more robust solution as apposed to

```
        if(i=='(' or i=='{' or i=='[')
```

since rather than increasing the if statement logic, we can just add another parenthesis pair within the hash.

## Using The Stack

We would use a stack in this case and for every time we encounter an open bracket, we add to stack.
Likewise, everytime we encounter a closing bracket that matches with the corresponding open bracket 
we can pop the open bracket from the stack since the parenthesis is resolved.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/c19d78e9-ce80-4345-a22c-8bd7ff704eb6)

This would mean that for every time we encounter an open parenthesis, we would append to the stack.

```
            op = "([{"
            if c in op:
                stack.append(c)
```

## False conditions:

The conditions are false when:
- A closing parenthesis is added when the stack is empty
  - This means that there is no open parenthesis for the closing one to recieve
```
                if not stack:
                    return False
```
- If the opening parentheis does not correspond with the current stacked parenthesis
```
                if brackets[stack[-1]] != brackets[c]:
                    return False
```
- If both these conditions are NOT satisified, we then check to see if the stack itself is empty since a non-empty stack
would mean there is atleast one extra open parenthesis.

```
                return not stack
```

Therefore, the final code would look like (Python): 

```
class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        brackets = {'(': 0, ')' : 0, '[': 1, ']' : 1, '{': 2, '}' : 2}
        stack = []

        for c in s:
            if c in op:
                stack.append(c)
            else:
                if not stack or brackets[stack[-1]] != brackets[c]:
                    return False
                stack.pop()
                    
        return not stack
```
