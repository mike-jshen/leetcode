# Find Minimum in rotated sorted array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Intuitive Solution

Without binary search, we could loop through each element of the array itself and constantly update the max value 
using the ```min()``` function.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/f090eb3f-3d93-4694-973a-85754da001fa)

The code would look something like this (Python pseudo-code):

```
import sys
arr = [3,4,5,6,0,1,2]
result = sys.maxsize

for num in arr:
  result = min(result,num)

return result
```
This would yield a time complexity of O(n) because we are looping through all the elements of the array given

However, since the array is assumed to be sorted but rotated we can apply a binary search algorithm to reduce 
time complexity.

## Refined solution using Binary Search

Using binary search principles, we can assign "left" and "right" pointers where ```mid = math.floor((left/right)/2)```

![image](https://github.com/mike-jshen/leetcode/assets/68671792/89bf3644-66ee-4ec6-a02c-24618429d885)

In the case that the right pointer is less than the mid value, we know that the minimum value must be inbetween them.

Therefore we will shift the left pointer the current mid and find the new mid inbetween.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/4fe6e74c-a5a4-46a9-8e17-04e98116a5d5)

```
if arr[mid] > arr[r]
  l = mid + 1
  mid = math.floor((left/right)/2)
```
If the first condition is not satisfied, we must then check if the left value is greater than the current mid value.
We know that the minium must be within the left and mid pointer as the array must start back at its minimum in order for the mid to be less than left pointer.

```
if arr[mid] < arr[l]
  r = mid
  mid = math.floor((left/right)/2)
```

NOTE: in the case that mid so happens be the minimum value within the array, we still ensapsulate the element by setting ```r = mid```

![image](https://github.com/mike-jshen/leetcode/assets/68671792/3bcbf90c-232f-41cb-a2e0-903919b600fb)

If none of these conditions are met, that means that

```
arr[l] < arr[mid] < arr[r]
```
which means that the array between l and r is in its sorted state. Thus, arr[l] should be the smallest element.

Continuing the first example:
![image](https://github.com/mike-jshen/leetcode/assets/68671792/0da73230-8c6e-4e36-b16a-f7c4e8c86cd4)

Where in this case, the left and right pointers encapsulate a sub-array: ```[0,1,2]``` so returing the first element of this subarray would be the smallest in the whole array.

Finally, I had accounted for the base case where the array is just one element. This would mean that the only element itself would be the minimum element within the array.

The code would look something like this:

```
def findMin(nums: List[int]) -> int:
  if len(nums) == 1:
    return nums[0]

  l = 0
  r = len(nums) - 1
  mid = math.floor((l+r)/2)
  while l < r:
    if nums[mid] > nums[r]:
      print("increase mid")
      l = mid + 1
      mid = math.floor((r+l)/2)

    elif nums[mid] < nums[l]:
      print("decrease mid")
      r = mid
      mid = math.floor((r+l)/2)
            
    else:
      return nums[l]
    
    return nums[mid]
```

Because this is binary search, the worst case scenario would be O(log n) if the pivot is near the middle and the best case would be O(1) if the array is not rotated.
