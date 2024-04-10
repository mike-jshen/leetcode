# Product Sales Analysis I
https://leetcode.com/problems/product-sales-analysis-i
```
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
 

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
 

Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.
```
## Select from the appropriate columns
Our output consists of: ```product_name``` from the Product table, and ```year``` and ```price``` from Sales table.
Using the SELECT statement in SQL, we can select the specific table attributes as follows:

```sql
SELECT Product.product_name, Sales.year, Sales.price FROM Product, Sales
```
### Shorthand Notation:
In this case, we can naturally express an INNER JOIN function by using a WHERE clause.
```sql
WHERE Sales.product_id = Product.Product_id;
```

## Code:
```sql
SELECT Product.product_name, Sales.year, Sales.price FROM Sales,
Product WHERE Sales.product_id = Product.Product_id;
```

