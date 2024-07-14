import requests
import pandas as pd
import json
import decimal
import functions

# Make a request to GET the data from the FPL API
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
response = requests.get(url)
data = json.loads(response.text)
df = pd.DataFrame.from_dict(data['elements'])

# Come back and make integers of all numerical columns
df['points_per_game'] = df['points_per_game'].apply(decimal.Decimal)
df['now_cost'] = df['now_cost'].apply(decimal.Decimal)/10

df['ppg_per_euro'] = df['points_per_game']/df['now_cost']
df['ppg_per_euro'] = df['ppg_per_euro'].astype(float).round(3)

teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Liverpool",
    "Luton Town",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sheffield United",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers"
]

functions.choose_metric(df, teams)
# print(df[df['ppg_per_euro'] != 0]['ppg_per_euro'].mean())
# print(df['points_per_game'].mean())
# functions.get_player_ranking(df, 'total_points', 'Palmer')


