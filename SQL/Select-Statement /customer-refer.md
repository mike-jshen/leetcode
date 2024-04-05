# Find Customer Referee
https://leetcode.com/problems/find-customer-referee
Table: Customer
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
```

Find the names of the customer that are not referred by the customer with id = 2.

## Select statement
Use the select statement to only print out "name" column

```SELECT name FROM Customer```

## WHEN statement

Use WHEN statement to check if ID is not equal to 2 OR ID is not equal to NULL

``` WHEN refree_id != 2 OR refree_id IS NOT NULL;```

## Code
```SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;```
