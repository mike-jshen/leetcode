# Longest Substring
https://leetcode.com/problems/longest-substring-without-repeating-characters
## Intuitive Solution
One of the intuitive solutions that first came to mind was to create a temporary substring in the form of an array and constantly update the left side of sliding window once a repeat character is enocuntered.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/a3d14d10-cbf8-4242-9dc1-878cc5c9028b)


Throughout every iteration of the substring, we are updating the length with max(length,substr.length()) to ensure that the max length is maintained.

Code would look like this (Java):

```
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int result = 0, left = 0;
        ArrayList<Character> substr = new ArrayList<Character>();
        
        for (int i = 0; i < s.length(); i++){
            while(substr.contains(s.charAt(i))){
                substr.remove(0);
                left++;
            }
                substr.add(s.charAt(i));
                result = Math.max(result, i - left + 1);
        }
        return result;
    }
}
```

This would give a runtime of O(n^2) in the worst case if none of the characters are repeating since the ```.contains``` method would be running within the whole string again after each character input.

## Refined Solution with HashMaps
We can negate this runtime by implementing a hashmap solution where the left side of the sliding window is stored and updated using a hashmap.

For every unique character that does not exist within the HashMap, we add the key as a character and its index with the corresponding value pair.

Every time we encounter a repeat character within the string, we update the left side of the window either replacing it with the next element of the previous index within the hash, or keep the current left side if it is greater.

![image](https://github.com/mike-jshen/leetcode/assets/68671792/8712d5a4-2919-4fb7-87eb-7c3f08ae68c9)

This would have a runtime of O(n) as extracting and updating the hash value within the loop would only take O(1) time.

```
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
```
