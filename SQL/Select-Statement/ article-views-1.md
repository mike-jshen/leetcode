# Article Views 1
https://leetcode.com/problems/article-views-i
```
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.
```
## USING AS Statement
When making a new column, we use the ```AS -n``` command where -n is the name of the output database.
Since they want a result table labled as "id", the code would be:

```IMPORT Views AS id```.

Satisfiying the own viewer logic is a simple compairson of both author_id and viewer_id 

```
WHERE author_id = viewer_id
```

Finally, the table is required to be sorted in ascending order so we use the ```ORDER BY``` command:

```
ORDER BY id ASC;
```
## Final Code:
```
SELECT DISTINCT author_id AS id FROM Views WHERE author_id = viewer_id ORDER BY id ASC;
```
