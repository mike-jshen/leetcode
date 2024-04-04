# Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas
## Intuition
The essense of this question is to find out the minimum divisor for each number in the array such that
the sum of the numbers confine to the input number.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/317fd6c9-38b1-42c0-899b-c1f3827748a8)

Since koko loves taking his sweet time when finishing with a pile, this means that he aint gonna be doing anything 
after he finishes with each pile (element in the array). This means that for each division value, we must take the
ceil to account for the remainder.

The intuitive thing would be to loop "M" through each number from 1 to max(arr) which would be 11 in this case and 
the moment "h" is equal to the sum of all the values, we output the corresponding "M" value.

This is inefficient as the worst case would be the max integer itself if the array cannot be dividied any lower.
Which would yield us a time complextiy of O(n^2).... NOT GOOD.

## Binary Search Solution:
This is where binary search comes into play. Insetad of looping through each number, we can use binary search 
principles to achieve the number we want.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/bb210c92-b1b5-47e7-81f2-36ff3bffb840)

## Application
In our case, we would make a numberline between 1 and the pile with the highest number (max(arr)) and calculate mid.

```
    l = 1
    r = max(piles)
    k = math.floor((l+r)/2)
```

For binary search, we know that l < r. The catch is that during the while loop, we must find the summation of each
element according to whichever mid value we have at the moment.

```
    while l < r:
        temp = 0
        for num in piles:
            temp += math.ceil(num/k)
```

What the for loop above is doing is essentially finding the sum of each divided element and storing it in ```temp```.

The image below visualizes the logic statement.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/6ac99ef2-d536-4d13-9df1-952c3e6d7c53)
From now on, I will refer ```temp``` as "sum".

Now we get to the binary search part of this problem.

If the sum is less than or equal to the given "h", then we know that the divisor is currently too big and must be 
decreased in order to decrease the sum.

```
        if temp <= h:
            r = k
            k = math.floor((r+l)/2)
```
Thus, in our code, we must set the right side to equal to the midpoint and calculate the new midpoint.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/d8a61ff1-f860-4dd0-ad46-62013d38397e)


Vice versa, if the sum is greater than the given "h", we know the divisor is currently too small and must be 
increased in order to decrease the sum.

```
        elif temp > h:
            l = k + 1
            k = math.floor((r+l)/2)
```
Conversly, we set the left side to equal our mid + 1 and calculate the new mid value.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/217c9441-551f-4a30-a373-d04d557bc7f3)

## Why do temp <= h?
Technically within the logic, we can just return the temp midpoint value the moment they equal. However,
in order to account for edge cases such as the array only being two elements long, we must continue with
the logic in order to account for any missing values.

Finally the code would look like:

```
def minEatingSpeed(piles: list[int], h: int) -> int:
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

arr = [3,6,7,11]
print(minEatingSpeed(arr, 8))
```
