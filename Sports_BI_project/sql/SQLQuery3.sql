USE SportsBI;
GO

SELECT COUNT(*) AS TotalMatches
FROM Matches;

SELECT COUNT(*) AS TotalTeamRecords
FROM teamMatches;

SELECT DISTINCT team
FROM teamMatches
ORDER BY team;