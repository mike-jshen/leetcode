# Customer Who Visited but Did Not Make Any Transactions
https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions
```
Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.
 

Table: Transactions

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.
 

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.
```
## Select Appropraite Columns and Using COUNT 
In this case, we only need the customer_id column from the Visits table. When it comes to counting the number of transactions, we use
the COUNT function to count the number of transactions.

```sql
SELECT Visits.customer_id, COUNT(Visits.visit_id) as count_no_trans FROM Visits
```
## Use LEFT JOIN
In this case, we are looking for the number of jpeople who made a visit without conducting a Transaction. This means that the column will
appear on the Visits table but not necessarily on the Transactions table.

Thus, we would use a LEFT JOIN where the Visits table is the left table to ensure that all values in Visits are accounted for.
```sql
FROM Visits LEFT JOIN Transactions
```
Since we are looking for the respective customer who did the visit, we must compare both visit_id columns in both tables.
```sql
ON Visits.visit_id = Transactions.visit_id
```

## IS NULL Operator
We then check when the Trancactions is null to find out when customers did not visit and group by visits to ensure that the 
number of visits with the customer_id is counted.
```sql
WHERE Transactions.visit_id IS NULL GROUP BY Visits.customer_id;
```

## Code:
```sql
SELECT Visits.customer_id, COUNT(Visits.visit_id) as count_no_trans
FROM Visits LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id IS NULL GROUP BY Visits.customer_id;
```
