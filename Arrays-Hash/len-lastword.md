# Length of Last Word
https://leetcode.com/problems/length-of-last-word

## Intuitive solution
Reverse loop through the array and check for an empty space after the last character is encountered.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/93f2b0fa-3bec-4164-a5c6-94e2cf90d815)

In the image example above, we start iterating at the "y" char and keep incrementing the counter until we hit the space.
The counter would then output the value of "6". 

Code would be: 
```
        count = 0
        for c in reversed(s):
            if c == ' ':
                return count
            elif c != ' ':
                result += 1
```

## Edge cases

### Speces before the string
- What if there are spaces after the last word of the string?
  - In this case, we would add a condition to the first statement stating that the count > 0 so that the logic
will skip through all spaces until the first word(character) is encountered.

- What if there are NO spaces?
  - In this case, we can return the count outside of the loop which would just yield the length of the string itself.

 With the added logic to account for edge cases the code would be:
 ```
        for c in t:
            if c == ' ' and count > 0:
                return count
            elif c != ' ':
                count += 1
         return count
```
