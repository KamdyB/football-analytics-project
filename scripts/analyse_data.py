# import pandas for dataframe manipulation
import pandas as pd

# read in the csv's to this file
schedule = pd.read_csv("data\championship_schedule_2024_25.csv")
player_stats = pd.read_csv("data\championship_player_stats_2024_25.csv")

# peek into the datasets I loaded
print(schedule.head())
print(player_stats.head())

# view the size of my datasets
print(schedule.shape)
print(player_stats.shape)

# look at the colun names
print(schedule.columns)
print(player_stats.columns)

# inspect the accuracy of data types
print(schedule.info())
print(player_stats.info())

# spot the total missing values
print(schedule.isna().sum())
print(player_stats.isna().sum())

# see if the numbers in the table make sense
print(schedule.describe())
print(player_stats.describe())