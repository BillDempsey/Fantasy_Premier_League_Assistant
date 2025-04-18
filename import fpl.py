import requests
import pandas as pd
import json
import functions
import os

file_names = ['24-25.xlsx', '23-24.xlsx', '22-23.xlsx', '21-22.xlsx', '20-21.xlsx', '19-20.xlsx']

# Pull in the current FPL data and save it under the first file name i.e. '24-25.xlsx'
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
response = requests.get(url)
data = json.loads(response.text)
current_season_data = pd.DataFrame.from_dict(data['elements'])
if os.path.exists(file_names[0]):
    print(f"{file_names[0]} already exists and will be overwritten.")
current_season_data.to_excel(file_names[1], index=False)
print(f"Current season data has been saved to {file_names[0]}.")

dataframes = [pd.read_excel(file) for file in file_names]

for df in dataframes:
    functions.sort_out_columns(df)

functions.store_historical_data(*dataframes)

teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Ipswich Town",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Southampton",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers"
]


functions.choose_metric(teams, dataframes[0])   # Display top performers based on current season
# print(df[df['ppg_per_euro'] != 0]['ppg_per_euro'].mean())
# print(df['points_per_game'].mean())
#functions.get_player_ranking(df_current, 'total_points', 'Palmer')


