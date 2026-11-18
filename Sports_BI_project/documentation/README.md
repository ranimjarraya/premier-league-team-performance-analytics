# Premier League Team Performance Analytics

## Project Overview

This project analyzes English Premier League match data using Business Intelligence and data analytics techniques.

The objective is to transform raw football match statistics into meaningful insights about team performance, attacking efficiency, defensive strength, and home-versus-away performance.

The analysis covers 100 matches involving 20 teams from the 2026/27 Premier League season dataset snapshot.

## Data Source

- **Source:** Open Matchday GitHub Repository
- **Competition:** English Premier League
- **Season:** 2026/27
- **Dataset size:** 100 matches
- **Teams:** 20

Dataset:
https://github.com/oladeeayo/open-matchday

The dataset contains match-level information, including scores, shots, shots on target, corners, fouls, cards, and match results.

Note: The analysis uses the available dataset snapshot and does not represent the complete 2026/27 season.

## Business Objectives

The project aims to answer the following questions:

1. Which teams demonstrate the strongest attacking performance?
2. Which teams have the strongest defensive performance?
3. Which teams generate the highest number of shots?
4. Which teams have the best shooting accuracy?
5. Does a higher number of shots lead to more goals?
6. How does team performance differ between home and away matches?
7. How does a selected team's performance evolve across matches?

## Tools and Technologies

- **Python:** Data exploration, cleaning, transformation, and analysis.
- **Pandas:** Data manipulation and preparation.
- **SQL Server:** Data storage, querying, aggregation, and performance analysis.
- **Power BI:** Interactive dashboards, data visualization, and DAX measures.
- **DAX:** KPI calculations and analytical measures.
- **GitHub:** Original dataset source.

## Project Workflow

### 1. Data Exploration

- Inspected the raw dataset.
- Reviewed column types, missing values, and data quality.
- Identified the main performance indicators.

### 2. Data Cleaning and Transformation

- Converted match dates into appropriate date formats.
- Standardized team names.
- Created match identifiers and calculated match-level indicators.
- Restructured the data into a team-match format, allowing each team to be analyzed independently.
- Validated scores, shots, and other key fields.

### 3. SQL Analysis

- Imported the prepared datasets into SQL Server.
- Created analytical queries for team rankings.
- Compared attacking and defensive performance.
- Analyzed home-versus-away results.

### 4. Power BI Development

- Connected Power BI to SQL Server.
- Created relationships between match-level and team-level tables.
- Developed DAX measures.
- Built a three-page interactive dashboard.

## Key Performance Indicators

| KPI             | Calculation                             |
| --------------- | --------------------------------------- |
| Total Goals     | Sum of goals scored by all teams        |
| Goals per Match | Total Goals / Total Matches             |
| Wins            | Number of matches won                   |
| Draws           | Number of matches drawn                 |
| Losses          | Number of matches lost                  |
| Goal Difference | Goals Scored - Goals Conceded           |
| Shot Accuracy   | Shots on Target / Total Shots           |
| Goal Conversion | Goals Scored / Total Shots              |
| Points          | 3 for a win, 1 for a draw, 0 for a loss |

## Key Findings

The analysis revealed several interesting insights:

- **Best attacking output:** Brighton scored 26 goals in 10 matches.
- **Strongest defence:** Arsenal conceded only 5 goals.
- **Best shooting accuracy:** Chelsea achieved 41.91%.
- **Best goal conversion:** Brighton achieved 15.38%.
- **Efficiency opportunity:** Manchester United attempted 193 shots but recorded a goal conversion rate of only 7.25%.

The comparison demonstrates that a high volume of shots does not necessarily translate into effective goal scoring.

## Dashboard Structure

The Power BI report contains three interactive pages:

### Page 1 — League Overview

- Overall competition KPIs.
- League points ranking.
- Goals scored by team.
- Goals conceded by team.

### Page 2 — Attacking Performance

- Shooting accuracy comparison.
- Goal conversion comparison.
- Shot volume versus goals scored.
- Home versus away attacking performance.
- Key analytical insights.

### Page 3 — Team Performance Deep Dive

- Team-specific wins, draws, and losses.
- Goal difference.
- Goals scored versus goals conceded.
- Points earned across gameweeks.
- Home versus away results.
- Shots taken against each opponent.

## Limitations

- The analysis is based on a snapshot of 100 matches, not the complete 2026/27 Premier League season.
- The dataset focuses on team and match statistics rather than individual player performance.
- Training sessions, player tracking, injuries, and other contextual factors are not included.
- Findings should be interpreted within the available sample.
