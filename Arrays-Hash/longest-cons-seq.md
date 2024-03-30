# Longest Consecutive Subsequence 
https://leetcode.com/problems/longest-consecutive-sequence

## Intuitive Approach

My initial thoughts upon this solution was to first sort the array itself using ```.sort()``` and then consecutively check to see if the next 
element within the array is equal to the current one. We would keep checking until the next element isent consecutive and repeat for each element.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/a4f84ef7-15b2-4276-999b-a1d20f313502)

The algorithm would look something like this (Python):

```
arr = [9,1,4,7,3,-1,0,5,8,-1,6]
arr.sort()
result = 0
for num in arr:
    count = 1
    temp = num + 1
    while temp in arr:
        count += 1
        temp += 1
    result = max(result,count)    
print(result)

```

EDIT: Sorting is not necessary in this case as we are just cheking to see if the consecutive number exists for however many times within the while loop.

In the worst case, the inner loop would iterate through all numbers in "arr" n times for each number. The outer loop also has a runtime of O(n) since we 
are iterating through each element in "arr" regardless.

Thus, the time complexity would be O(n^2). NOT VERY EFFICIENT and does not meet the O(n) time complexity quota stated within the question.

## Refined solution using Python Sets

