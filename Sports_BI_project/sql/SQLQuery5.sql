USE SportsBI;
GO

SELECT
    team,

    SUM(goals_for) AS goals_scored,
    SUM(goals_against) AS goals_conceded,

    SUM(shots) AS total_shots,
    SUM(shots_on_target) AS shots_on_target,

    ROUND(
        SUM(shots_on_target) * 100.0 /
        NULLIF(SUM(shots), 0), 2
    ) AS shot_accuracy,

    ROUND(
        SUM(goals_for) * 100.0 /
        NULLIF(SUM(shots), 0), 2
    ) AS goal_conversion,

    ROUND(
        SUM(goals_for) * 1.0 /
        COUNT(*), 2
    ) AS goals_per_match

FROM teamMatches

GROUP BY team

ORDER BY goals_scored DESC;