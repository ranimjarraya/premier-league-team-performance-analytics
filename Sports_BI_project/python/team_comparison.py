import pandas as pd

# Load team-level match data
df = pd.read_csv("data/team_matches.csv")

# Select the two teams
teams = ["Arsenal", "Brighton"]
comparison = df[df["team"].isin(teams)].copy()

# Calculate performance indicators
summary = comparison.groupby("team").agg(
    matches=("match_id", "count"),
    wins=("result", lambda x: (x == "Win").sum()),
    goals_scored=("goals_for", "sum"),
    goals_conceded=("goals_against", "sum"),
    total_shots=("shots", "sum"),
    shots_on_target=("shots_on_target", "sum"),
    home_matches=("venue", lambda x: (x == "Home").sum()),
    away_matches=("venue", lambda x: (x == "Away").sum())
).reset_index()

summary["shot_accuracy"] = (
    summary["shots_on_target"] / summary["total_shots"] * 100
).round(2)

summary["goals_per_match"] = (
    summary["goals_scored"] / summary["matches"]
).round(2)

summary["goals_per_shot"] = (
    summary["goals_scored"] / summary["total_shots"] * 100
).round(2)

print("\n===== ARSENAL VS BRIGHTON =====")
print(summary.to_string(index=False))

# Compare home and away performance
venue_summary = comparison.groupby(
    ["team", "venue"]
).agg(
    matches=("match_id", "count"),
    goals_scored=("goals_for", "sum"),
    goals_conceded=("goals_against", "sum"),
    points=("points", "sum")
).reset_index()

print("\n===== HOME VS AWAY PERFORMANCE =====")
print(venue_summary.to_string(index=False))

# Save results
summary.to_csv("data/team_comparison.csv", index=False)
venue_summary.to_csv("data/home_away_comparison.csv", index=False)

print("\nCOMPARISON COMPLETE!")