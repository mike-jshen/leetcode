# Longest Consecutive Subsequence 
https://leetcode.com/problems/longest-consecutive-sequence

[Algorithm Inspiration](https://www.youtube.com/watch?v=P6RZZMu_maU)

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

## Refined algorithm approach (Check previous integer)

The first thing we could check before we even start using sets is to check if a number that comes before exists.
Since we know that each consequetive sequence must start at a number, the first number for each sequence cannot have ```n - 1``` before it. 

We then periodically update the result with the max that is calculated for each consecutive sequence.

Thus, the the code becomes: 

```
for num in arr:
    if temp - 1 not in arr:
        count = 1
        temp = num + 1
        while temp in arr:
            count += 1
            temp += 1
        result = max(result,count)
```
However, this still yeilds a O(n^2) time complexity in the worst case when all elements within the array are in some consecutive order. 

## Refined Solution using Python Sets (Hashing)

Thus, we will use the same algorithm but rather than iterating through an array, we can use a Python set since indexing only takes O(1) time.

```
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
s = set(nums)
result = 0

    for num in s:
        if num - 1 not in s:
        count = 1
        temp = num + 1

        while temp in s:
            count += 1
            temp += 1
    result = max(result,count)
```

In this case, the worst case itself would be the length of consecutive numbers which we will denote as "m". This would make the average runtime O(n + m).

In the worst case where every element is a consecutive number, we would go through every element in the set which 
would set 'm' as 'n' and give us a time complexity of O(n + n) which simplifies to O(n).



