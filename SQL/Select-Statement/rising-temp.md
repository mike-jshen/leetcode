# Rising Temperature
https://leetcode.com/problems/rising-temperature
```
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 

Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.
```

## Using DATEDIFF
In this case, we use the function DATEDIFF() to find out the difference in days.
For example:
```sql
SELECT DATEDIFF('2017/08/25', '2017/08/26') AS DateDiff;
```
will yield the number 1. Since we want to find the previous day, then the 
DATEDIFF function must have a value of 1.

## Join own table:
Since there is only one table that is presented with us, we can use JOIN to join the
table within itself. 
```sql
SELECT w1.id FROM Weather w1 JOIN Weather w2 ON
```
In this example, w1 is the current day and w2 is the previous day.

Since we are outputting the id, we then extract w1.id and compare the recordDate on w1 and w2.
```sql
DATEDIFF(w1.recordDate, w2.recordDate) = 1
```

## Temperature difference
We then must set a WHERE condition that denotes how the current day temperature is greater than 
the previous day.

```sql
WHERE w1.temperature > w2.temperature
```

## Code
```sql
SELECT w1.id FROM Weather w1 JOIN weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
```
