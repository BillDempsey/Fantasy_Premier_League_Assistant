import requests
import pandas as pd
import json
import decimal
import functions_historical

# Load in the 23-24 season just like this (it too, is a past season)
df_23_24 = pd.read_excel('23-24.xlsx')                              # TEST IF THIS EXCEL READS IN CORRECTLY. THE REST ARE GOOD.
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

initial_loading_work(df_23_24)
initial_loading_work(df_22_23)
initial_loading_work(df_21_22)
initial_loading_work(df_20_21)
initial_loading_work(df_19_20)

#functions_historical.choose_metric(df_19_20)
functions_historical.get_historical_data_strings("Erling Haaland", df_23_24, df_22_23, df_21_22, df_20_21, df_19_20)

