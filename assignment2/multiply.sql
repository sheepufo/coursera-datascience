-- Data Science
-- Assignment 2
-- Problem 2

-- SQL Matrix Multiplication

SELECT a.row_num, b.col_num, SUM(a.value*b.value)
FROM a,b
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num
HAVING a.row_num=2 AND b.col_num=3;

