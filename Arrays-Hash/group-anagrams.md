# Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

## Train of thought (Finding Anagrams)
In this case, I wanted to figure out how to store unique integer values for each word based on its corresponding 
character composition.

This would mean that each word would generate a unique key based on its character composition. In order to do that,
each letter within the alphabet would have to be assigned with a ***prime number***.

```
a = 'abcdefghijklmnopqrstuvwxyz'
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
d_map = dict(zip(a, p))
```

## Why use prime numbers?

We can use prime numbers to our advantage to save on computational space. Since prime numbers are not divisible by
any number except itself and 1, if we multiply any amount of prime numbers together, we will get a composite number
no matter what.

This ensures that no string key values would overlap with existing prime chacter values which is how 
we can derrive unique keys out of each corresponding string.

```
KEY             VALUE
"aab" = 2*2*3 = 12
No other composition of characters can have the product of 12. Although 4 is a divisor of 12,
since 4 is not a prime number, it cannot possibly overlap with any other chacter value.
```

If we find the total product of each chacter prime value, we can then check to see if the product total aligns with
an existing prime value. In order for two strings to have the same key value, they MUST be anagrams since they are
essentially being multiplied by the same prime numbers.

```
KEY             VALUE
"aab" = 2*2*3 = 12
"aba" = 2*3*2 = 12

Since the value is the same, both "aab" and "aba" must be anagrams.
```
## How does this save computational power?
With this provided, we do not need to check and compare character values of each string anymore which would take O(k^2).
Rather, we can just compute the unique product value of each string and do a quick INT compairson
which would take O(k) time complexity where 'k' is the length of the longest string.

## Applying this to our current 

