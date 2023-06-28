--52nd Solution
SELECT SUBMISSION_DATE,

(SELECT COUNT(DISTINCT HACKER_ID)
FROM SUBMISSIONS S2
WHERE S2.SUBMISSION_DATE = S1.SUBMISSION_DATE AND (SELECT COUNT(DISTINCT S3.SUBMISSION_DATE)
                                                   FROM SUBMISSIONS S3
                                                   WHERE S3.HACKER_ID = S2.HACKER_ID 
                                                   AND S3.SUBMISSION_DATE < S1.SUBMISSION_DATE)
 = DATEDIFF(S1.SUBMISSION_DATE, "2016-03-01")),
 
(SELECT HACKER_ID
FROM SUBMISSIONS S2
WHERE S2.SUBMISSION_DATE = S1.SUBMISSION_DATE
GROUP BY HACKER_ID
ORDER BY COUNT(SUBMISSION_ID) DESC, HACKER_ID 
LIMIT 1) AS SHIT, (SELECT NAME
                  FROM HACKERS
                  WHERE HACKER_ID = SHIT)
FROM (SELECT DISTINCT SUBMISSION_DATE
     FROM SUBMISSIONS) S1
GROUP BY SUBMISSION_DATE