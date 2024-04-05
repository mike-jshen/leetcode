# Recyclable and Low Fat Products
https://leetcode.com/problems/recyclable-and-low-fat-products
```
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.
```

## SELECT STATEMENT
If we want to encompass both low_fat and recyclebale, we must use an AND statment where the logic contains for 
both attributes and compare to see if they equal to 'Y'.

```
SELECT product_id from Products WHERE low_fats = 'Y' AND recyclable = 'Y';
```
