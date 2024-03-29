# Find Minimum in rotated sorted array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Intuitive Solution

Without binary search, we could loop through each element of the array itself and constantly update the max value 
using the max() function.

The code would look something like this (Python pseudo-code):

```
import sys
arr = [3,4,5,6,0,1,2]
result = -sys.maxsize

for num in arr:
  result = max(result,num)

return result
```
This would yield a time complexity of O(n) because we are looping through all the elements of the array given

However, since the array is assumed to be sorted but rotated we can apply a binary search algorithm to reduce 
time complexity.
