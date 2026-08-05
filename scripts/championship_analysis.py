# import pandas for dataframe manipulation
import pandas as pd

#import my utility function to clean headers
from fbref_utils import combine_fbref_headers

# read in the datasets to this file as 'raw' to this file
raw_player_stats = pd.read_csv("data/championship_player_stats_2024_25.csv",
                               header=None)

# peek into the datasets I loaded
print(raw_player_stats.head())

#look at the last few data entries
print(raw_player_stats.tail())

#sampling the data
print(raw_player_stats.sample())

# view the size of my datasets
print(raw_player_stats.shape)

# look at the colun names
print(raw_player_stats.columns)

# inspect the accuracy of data types
raw_player_stats.info()

# spot the total missing values
print(raw_player_stats.isna().sum())

# see if the numbers in the table make sense
print(raw_player_stats.describe())

#use imported function to clean column headers
player_stats = combine_fbref_headers(raw_player_stats)
print(player_stats.head())