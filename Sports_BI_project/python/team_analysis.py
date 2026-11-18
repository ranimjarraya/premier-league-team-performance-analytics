
import pandas as pd

# Load transformed team data
df = pd.read_csv("data/team_matches.csv")

# Group data by team and calculate KPIs
summary = df.groupby("team").agg(
    matches=("match_id", "count"),
    wins=("result", lambda x: (x == "Win").sum()),
    draws=("result", lambda x: (x == "Draw").sum()),
    losses=("result", lambda x: (x == "Loss").sum()),
    points=("points", "sum"),
    goals_scored=("goals_for", "sum"),
    goals_conceded=("goals_against", "sum"),
    total_shots=("shots", "sum"),
    shots_on_target=("shots_on_target", "sum"),
    total_corners=("corners", "sum"),
    total_fouls=("fouls", "sum"),
    yellow_cards=("yellow_cards", "sum"),
    red_cards=("red_cards", "sum")
).reset_index()

# Calculate additional KPIs
summary["goal_difference"] = (
    summary["goals_scored"] - summary["goals_conceded"]
)

summary["win_rate"] = (
    summary["wins"] / summary["matches"] * 100
).round(2)

summary["goals_per_match"] = (
    summary["goals_scored"] / summary["matches"]
).round(2)

summary["goals_conceded_per_match"] = (
    summary["goals_conceded"] / summary["matches"]
).round(2)

summary["shot_accuracy"] = (
    summary["shots_on_target"] / summary["total_shots"] * 100
).round(2)

summary["goal_conversion"] = (
    summary["goals_scored"] / summary["total_shots"] * 100
).round(2)

summary["avg_shots_per_match"] = (
    summary["total_shots"] / summary["matches"]
).round(2)

# Rank teams by points, goal difference, then goals scored
summary = summary.sort_values(
    by=["points", "goal_difference", "goals_scored"],
    ascending=[False, False, False]
).reset_index(drop=True)

summary.insert(0, "rank", range(1, len(summary) + 1))

# Save the summary
summary.to_csv("data/team_summary.csv", index=False)

# Display results
print("\n===== TEAM PERFORMANCE RANKING =====")
print(summary[
    ["rank", "team", "matches", "wins", "draws",
     "losses", "points", "goals_scored",
     "goals_conceded", "goal_difference"]
].to_string(index=False))

print("\n===== BEST ATTACK =====")
print(summary.nlargest(3, "goals_scored")[
    ["team", "goals_scored"]
].to_string(index=False))

print("\n===== BEST DEFENCE =====")
print(summary.nsmallest(3, "goals_conceded")[
    ["team", "goals_conceded"]
].to_string(index=False))

print("\n===== BEST SHOT ACCURACY =====")
print(summary.nlargest(3, "shot_accuracy")[
    ["team", "shot_accuracy"]
].to_string(index=False))

print("\nANALYSIS COMPLETE!")
print("Saved: data/team_summary.csv")
