# Invalid Tweets
https://leetcode.com/problems/invalid-tweets
```
Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.
 

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.
```

## Using CHAR_LENGTH
In this question, it is asking to output the rows in which the content length has a character value greater than 15

Thus, we would use the CHAR_LENGTH() function in order to extract the string length and compare it > 15.

Code:
```
SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content) > 15;
```
