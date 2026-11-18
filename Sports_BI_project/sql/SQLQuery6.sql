USE SportsBI;
GO

SELECT
    team,
    venue,

    COUNT(*) AS matches,

    SUM(goals_for) AS goals_scored,
    SUM(goals_against) AS goals_conceded,

    SUM(points) AS total_points,

    ROUND(
        SUM(points) * 1.0 / COUNT(*), 2
    ) AS points_per_match

FROM TeamMatches

GROUP BY team, venue

ORDER BY team, venue;