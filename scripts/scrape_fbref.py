import json
from pathlib import Path

# Path where soccerdata looks for config files
config_dir = Path.home() / "soccerdata" / "config"
config_dir.mkdir(parents=True, exist_ok=True)
config_file = config_dir / "league_dict.json"

# Load existing config or initialize empty dict
if config_file.exists():
    with open(config_file, "r") as f:
        try:
            leagues = json.load(f)
        except json.JSONDecodeError:
            leagues = {}
else:
    leagues = {}

# Map the internal FBref league identifier for English Championship
leagues["ENG-Championship"] = {
    "FBref": "EFL Championship"
}

# Save configuration
with open(config_file, "w") as f:
    json.dump(leagues, f, indent=4)

print(f"Config successfully updated at: {config_file}")

import soccerdata as sd

# Initialize scraper for the Championship
fbref = sd.FBref(leagues="ENG-Championship", seasons="2024-25")

# Pull match schedule/results
schedule = fbref.read_schedule()
print("--- Schedule Data ---")
print(schedule.head())

# Pull standard player stats
player_stats = fbref.read_player_season_stats(stat_type="standard")
print("--- Player Stats ---")
print(player_stats.head())

schedule.to_csv("championship_schedule_2024_25.csv")
player_stats.to_csv("championship_player_stats_2024_25.csv")

print("Files saved successfully to your project folder!")