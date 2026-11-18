
import pandas as pd

# Load cleaned match data
df = pd.read_csv("data/cleaned_matches.csv")

# HOME TEAM DATA
home = pd.DataFrame({
    "match_id": df["match_id"],
    "date": df["date"],
    "gameweek": df["gw"],
    "team": df["home"],
    "opponent": df["away"],
    "venue": "Home",
    "goals_for": df["ft_home"],
    "goals_against": df["ft_away"],
    "shots": df["home_shots"],
    "shots_on_target": df["home_target"],
    "fouls": df["home_fouls"],
    "corners": df["home_corners"],
    "corners_1h": df["home_corners_1h"],
    "corners_2h": df["home_corners_2h"],
    "yellow_cards": df["home_yellow"],
    "red_cards": df["home_red"]
})

# AWAY TEAM DATA
away = pd.DataFrame({
    "match_id": df["match_id"],
    "date": df["date"],
    "gameweek": df["gw"],
    "team": df["away"],
    "opponent": df["home"],
    "venue": "Away",
    "goals_for": df["ft_away"],
    "goals_against": df["ft_home"],
    "shots": df["away_shots"],
    "shots_on_target": df["away_target"],
    "fouls": df["away_fouls"],
    "corners": df["away_corners"],
    "corners_1h": df["away_corners_1h"],
    "corners_2h": df["away_corners_2h"],
    "yellow_cards": df["away_yellow"],
    "red_cards": df["away_red"]
})

# Combine home and away records
team_matches = pd.concat([home, away], ignore_index=True)

# Calculate match result from each team's perspective
team_matches["result"] = "Draw"

team_matches.loc[
    team_matches["goals_for"] > team_matches["goals_against"],
    "result"
] = "Win"

team_matches.loc[
    team_matches["goals_for"] < team_matches["goals_against"],
    "result"
] = "Loss"

# Calculate league points
team_matches["points"] = 0

team_matches.loc[team_matches["result"] == "Win", "points"] = 3
team_matches.loc[team_matches["result"] == "Draw", "points"] = 1

# Save the transformed data
team_matches.to_csv("data/team_matches.csv", index=False)

# Display results
print("\nTEAM DATASET PREVIEW")
print(team_matches.head(10))

print("\nDATASET SIZE")
print(team_matches.shape)

print("\nNUMBER OF TEAMS")
print(team_matches["team"].nunique())

print("\nMATCH RECORDS PER TEAM")
print(team_matches["team"].value_counts().sort_index())

print("\nRESULT DISTRIBUTION")
print(team_matches["result"].value_counts())

print("\nTRANSFORMATION COMPLETE!")
