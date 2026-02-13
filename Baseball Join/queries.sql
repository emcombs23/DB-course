--First Join Example
SELECT *
FROM batting
INNER JOIN teams ON batting.teamID = teams.teamID and batting.yearID = teams.yearID
WHERE batting.yearID = 1976 and playerID = 'schmimi01';

--player ids, and team names
SELECT playerID, name
FROM batting
INNER JOIN teams ON batting.teamID = teams.teamID and batting.yearID = teams.yearID
WHERE batting.yearID = 1976;

--Babe ruth home runs by year
SELECT batting.yearID, name, batting.HR
FROM batting
INNER JOIN teams ON batting.teamID = teams.teamID and batting.yearID = teams.yearID
WHERE playerID = 'ruthba01';