import requests
import pandas as pd
import json
import decimal
import functions_historical

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
response = requests.get(url)
data = json.loads(response.text)
df_current = pd.DataFrame.from_dict(data['elements'])
df_23_24 = pd.read_excel('23-24.xlsx') 
df_22_23 = pd.read_excel('22-23.xlsx')
df_21_22 = pd.read_excel('21-22.xlsx')
df_20_21 = pd.read_excel('20-21.xlsx')
df_19_20 = pd.read_excel('19-20.xlsx')

def initial_loading_work(df):
    df['points_per_game'] = df['points_per_game'].apply(decimal.Decimal)
    df['now_cost'] = df['now_cost'].apply(decimal.Decimal)/10
    df['ppg_per_euro'] = df['points_per_game']/df['now_cost']
    df['ppg_per_euro'] = df['ppg_per_euro'].astype(float).round(3)
    df['points_per_game'] = df['points_per_game'].astype(float).round(3)
    df['name'] = df['first_name'] + " " + df['second_name']

initial_loading_work(df_current)
initial_loading_work(df_23_24)
initial_loading_work(df_22_23)
initial_loading_work(df_21_22)
initial_loading_work(df_20_21)
initial_loading_work(df_19_20)

functions_historical.choose_metric(df_current, df_23_24, df_22_23, df_21_22, df_20_21, df_19_20)


