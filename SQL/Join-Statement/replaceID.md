# Replace Employee ID With The Unique Identifier
```
Table: Employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
 

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.
```
## Use FROM to extract at two tables
We use the expression ```SELECT EmployeeUNI.unique_id, Employees.name``` to take the specific attributes from each
respective table. This means that we take the unique_id column from EmployeeUNI and the name column from Employee.

## Use LEFT JOIN
In this case, we want to encapsulate all the values from the Employees table in order to satisfy the condition 
of replacing a unique ID with NULL if the ID does not exist. 

```SQL
Employees LEFT JOIN EmployeeUNI
```
## Check and output unique_id
We also want to check and compare the ID attributes from both the tables in order to output the correct unique ID
This would be a simple WHERE clause:
```SQL
WHERE Employees.id = EmployeeUNI.id
```

## Code:
```SQL
SELECT EmployeeUNI.unique_id, Employees.name FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
```

## RIGHT JOIN Solution
Conversly, we could use RIGHT JOIN to select the null values as we would just replace the position of "Employees" and "EmployeeUNI".
```SQL
SELECT EmployeeUNI.unique_id, Employees.name FROM EmployeeUNI
RIGHT JOIN Employees ON Employees.id = EmployeeUNI.id;
```
