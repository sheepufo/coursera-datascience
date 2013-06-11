-- Data Science
-- Assignment 2
-- Problem 1
--(a)
/*
SELECT count(*)
	FROM frequency
	WHERE docid = "10398_txt_earn";
*/

--(b)
/*
SELECT count(*)
	FROM frequency
	WHERE docid = "10398_txt_earn" and count = 1;
*/

--(c)
/*
SELECT count(*) 
	FROM (SELECT term FROM frequency 
			WHERE docid="10398_txt_earn" and count = 1
		UNION 
		SELECT term FROM frequency 
			WHERE docid="925_txt_trade" and count=1);
*/

--(d)
/*
SELECT count(*) FROM frequency
	WHERE term = "parliament";
*/

--(e)
/*
SELECT count(*) FROM (SELECT docid FROM frequency 
						GROUP BY docid 
						HAVING sum(count)>300);
*/

--(f)
SELECT count(*) FROM (SELECT docid FROM frequency 
						WHERE term = "transactions" 
					INTERSECT 
					SELECT docid FROM frequency 
						WHERE term = "world");







