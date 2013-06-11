-- Data Science
-- Assignment 2
-- Problem 3

--(h)
/*SELECT SUM(freq1.count*freq2.count)
FROM frequency AS freq1, frequency AS freq2
WHERE freq1.term = freq2.term
GROUP BY freq1.docid, freq2.docid
HAVING freq1.docid = "10080_txt_crude" AND freq2.docid = "17035_txt_earn"; 
*/

---(g)
---Computing similarity of query with all documents
/*CREATE VIEW query AS
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;
*/

SELECT MAX(sim.count) FROM 
(SELECT SUM(A.count*B.count) as count
FROM frequency AS A, query AS B
WHERE A.term=B.term
GROUP BY A.docid, B.docid) AS sim;











