
import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("data/premier_league_2026_27.csv")

print("ORIGINAL DATA:", df.shape)

# 2. Convert date into a proper date format
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 3. Clean team names
df["home"] = df["home"].str.strip()
df["away"] = df["away"].str.strip()

# 4. Create a unique match ID
df["match_id"] = range(1, len(df) + 1)

# 5. Create new performance indicators
df["goal_difference_home"] = df["ft_home"] - df["ft_away"]
df["goal_difference_away"] = df["ft_away"] - df["ft_home"]

df["total_goals"] = df["ft_home"] + df["ft_away"]
df["total_shots"] = df["home_shots"] + df["away_shots"]

# 6. Check data quality
print("\nDATE ERRORS:")
print(df["date"].isnull().sum())

print("\nINVALID TEAM NAMES:")
print((df["home"] == "").sum() + (df["away"] == "").sum())

print("\nINVALID SCORES:")
print(((df["ft_home"] < 0) | (df["ft_away"] < 0)).sum())

print("\nSHOT VALIDATION:")
print("Home shots on target exceeding shots:",
      (df["home_target"] > df["home_shots"]).sum())

print("Away shots on target exceeding shots:",
      (df["away_target"] > df["away_shots"]).sum())

# 7. Save cleaned data
df.to_csv("data/cleaned_matches.csv", index=False)

print("\nCLEANING COMPLETE!")
print("Cleaned dataset saved in data/cleaned_matches.csv")
print("Final dimensions:", df.shape)
