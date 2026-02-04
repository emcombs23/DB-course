--Find 10 Playes with most HRs
SELECT playerID, SUM(HR) as HRs
FROM batting
GROUP BY playerID
ORDER BY HRs desc
LIMIT 10;
--Year by year HRs for the Phillies
SELECT yearID, SUM(HR) as HRs
FROM batting
WHERE teamID = 'PHI'
GROUP BY yearID
ORDER BY yearID;