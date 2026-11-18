USE SportsBI;
GO

WITH TeamStats AS (
    SELECT
        team,
        COUNT(*) AS matches,

        SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) AS wins,
        SUM(CASE WHEN result = 'Draw' THEN 1 ELSE 0 END) AS draws,
        SUM(CASE WHEN result = 'Loss' THEN 1 ELSE 0 END) AS losses,

        SUM(points) AS points,
        SUM(goals_for) AS goals_scored,
        SUM(goals_against) AS goals_conceded,

        SUM(goals_for) - SUM(goals_against) AS goal_difference

    FROM teamMatches
    GROUP BY team
)

SELECT
    ROW_NUMBER() OVER (
        ORDER BY points DESC,
                 goal_difference DESC,
                 goals_scored DESC
    ) AS rank,

    team,
    matches,
    wins,
    draws,
    losses,
    points,
    goals_scored,
    goals_conceded,
    goal_difference

FROM TeamStats
ORDER BY rank;