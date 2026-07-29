# import pandas for dataframe manipulation
import pandas as pd

# read in the csv's to this file
schedule = pd.read_csv("data\championship_schedule_2024_25.csv")
player_stats = pd.read_csv("data\championship_player_stats_2024_25.csv")

# view the coordinate size of the two datasets
print("Schedule Shape")
print(schedule.shape)
print("\nPlayer Stats Shape")
print(player_stats.shape)

# view all column headers for two datasets
print(schedule.columns)
print(player_stats.columns)

# view the datatypes of the datsets
print(schedule.dtypes)
print(player_stats.dtypes)

# check for missing values
print(schedule.isnull().sum())
print(player_stats.isnull().sum())

# check specified missing value categories and draw a pattern
print(schedule[schedule['week'].isna()])
print(player_stats[player_stats.isnull().any(axis=1)])
print(player_stats.loc[[348,458,597,718]].T)
print(player_stats[player_stats['nation'].isna()])
print(player_stats[player_stats['age'].isna()])

# remove the two FBref header rows that were saved as data
player_stats = player_stats.iloc[2:].reset_index(drop=True)

# check missing values after removing the fake rows
print(player_stats.isnull().sum())

# rename generic column names to meaningful football names
player_stats.rename(columns={
    "Unnamed: 0": "league",
    "Unnamed: 1": "season",
    "Unnamed: 2": "team",
    "Unnamed: 3": "player",
    "Playing Time": "matches",
    "Playing Time.1": "starts",
    "Playing Time.2": "minutes",
    "Playing Time.3": "ninetys",
    "Performance": "goals",
    "Performance.1": "assists",
    "Performance.2": "goal_contrib",
    "Performance.3": "np_goals",
    "Performance.4": "pen_goals",
    "Performance.5": "pen_attempts",
    "Performance.6": "yellow_cards",
    "Performance.7": "red_cards",
    "Per 90 Minutes": "goals_p90",
    "Per 90 Minutes.1": "assists_p90",
    "Per 90 Minutes.2": "goal_contrib_p90",
    "Per 90 Minutes.3": "np_goals_p90",
    "Per 90 Minutes.4": "np_goal_contrib_p90"
}, inplace=True)

print(player_stats.head())