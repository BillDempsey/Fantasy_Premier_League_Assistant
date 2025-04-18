#### functions.py
import decimal
from fuzzywuzzy import process

# Function to take user input which chooses the metric to sort by...
# ... the number of players to display this for...
# ... and calls the relevant function to do so.
def choose_metric(league_teams, dataframe):
    chosen_metric = input("Choose one of the following metrics to display:\ntotal_points\npoints_per_game\nPPGPE\nep_this\nep_next\n\n") # include try/catch for anything other than strings (already done in function? Better to do it here.)
    nplayers = int(input("\nChoose how many players you want displayed:\n\n"))  # Include try/catch for anything other than positive integers

    if chosen_metric == 'PPGPE':
        nplayers_PPGE(nplayers, league_teams, dataframe)
    elif chosen_metric == 'points_per_game':
        nplayers_PPG(nplayers, league_teams, dataframe)
    elif chosen_metric == 'total_points':
        nplayers_total_points(nplayers, league_teams, dataframe)
    elif chosen_metric == 'ep_this':
        nplayers_ep_this(nplayers, league_teams, dataframe)
    elif chosen_metric == 'ep_next':
        nplayers_ep_next(nplayers, league_teams, dataframe)
    else:
        print('Invalid output for "metric" field')  # Maybe swap this for an earlier try/catch

##################################################################################################################################
# All the functions which print out the n players leading the chosen metric

def nplayers_PPGE(nplayers, league_teams, dataframe):
    answer = int(input("\nWhat is the minimum number of points you want the players on display to have?\n\n"))
    ordered = dataframe.sort_values('ppg_per_euro', ascending=False)
    filtered = ordered[ordered['total_points'] > answer]
    top_n = filtered.head(nplayers)
    for i in top_n.index:
        playername = dataframe.loc[i, 'name']
        player_report(playername, league_teams, dataframe)

def nplayers_PPG(nplayers, league_teams, dataframe):
    top_n = dataframe.sort_values('points_per_game', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(playername, league_teams, dataframe)

def nplayers_total_points(nplayers, league_teams, dataframe):
    top_n = dataframe.sort_values('total_points', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(playername, league_teams, dataframe)

def nplayers_ep_this(nplayers, league_teams, dataframe):
    top_n = dataframe.sort_values('ep_this', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(playername, league_teams, dataframe)

def nplayers_ep_next(nplayers, league_teams, dataframe):
    top_n = dataframe.sort_values('ep_next', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(playername, league_teams, dataframe)

##################################################################################################################################
# Find a player by name in the dataframe and print out their data

def player_report(playername, league_teams, dataframe):
    # Include try/catch here, checking a) if the name exists b) if it's a duplicate
    # Maybe use combination of first and surnames instead in time

    # Set up a kind of fuzzy match to catch the names if spelled incorrectly. 
    # Also account for 2 similar/same names
    try:
        player = dataframe[dataframe['name'] == playername].iloc[0]
    except IndexError:
        print(f"Player named {playername} not found.")
        return

    position = {1: 'GK', 2: 'Def', 3: 'Mid', 4: 'Fwd'}
    
    player_element_type = int(player['element_type'])
    player_team_index = int(player['team']) - 1
    print(" \n")
    print(f"Player:\t\t {player['name']}\n"
          f"Position:\t {position[player_element_type]}\n"
          f"Team:\t\t {league_teams[player_team_index]}\n"
          f"Points:\t\t {player['total_points']} \t\t\t({get_player_ranking(dataframe,'total_points', playername)})\n"
          f"Cost:\t\t {player['now_cost']:.1f} \t\t\t({get_player_ranking(dataframe,'now_cost', playername)})\n"
          f"PPG:\t\t {player['points_per_game']} \t\t\t({get_player_ranking(dataframe,'points_per_game', playername)})\n"
          f"PPGPE:\t\t {player['ppg_per_euro']:.3f} \t\t\t({get_player_ranking(dataframe,'ppg_per_euro', playername)})\n"
          f"EP this:\t {player['ep_this']} \t({player['chance_of_playing_this_round']}%) \t({get_player_ranking(dataframe,'ep_this', playername)})\n"
          f"EP next:\t {player['ep_next']} \t({player['chance_of_playing_next_round']}%) \t({get_player_ranking(dataframe,'ep_next', playername)})"
          )
    print_history(player, dataframe)
    # return player

#######################################################

def get_player_ranking(dataframe, metric, playername):
    sorted_df = dataframe.sort_values(metric, ascending=False)
    sorted_df.reset_index(drop=True, inplace=True) # Reset the index of the sorted DataFrame so that the positions reflect the new order
    try:
        player_index = sorted_df[sorted_df['name'] == playername].index[0]
    except IndexError:
        print(f"Player named {playername} not found by get_player_ranking() function.")
        return None
    ranking = player_index + 1
    return ranking

#############################################

def print_history(playername, df_current):
    def get_player_data(playername, df_current):

        try:
            # Perform fuzzy matching
            names_list = df_current['name'].tolist()  # Get all names as a list
            match, score = process.extractOne(playername, names_list)  # Find the best match
            
            if score > 80:  # Adjust threshold as needed
                player_row = df_current[df_current['name'] == match]
                return player_row.iloc[0]
            else:
                print(f"No close match found for {playername}")

        except Exception as e:
            print(f"Error occurred: {e}")
            return None

    # Define the historical data columns
    historical_data = [
        ("2023_24", "total_points_2023_24", "PPG_2023_24"),
        ("2022_23", "total_points_2022_23", "PPG_2022_23"),
        ("2021_22", "total_points_2021_22", "PPG_2021_22"),
        ("2020_21", "total_points_2020_21", "PPG_2020_21"),
        ("2019_20", "total_points_2019_20", "PPG_2019_20")
    ]

    output = ""
    
    for season_label, total_points_col, ppg_col in historical_data:
        player_data = get_player_data(playername, df_current)
        if player_data is not None:
            points = player_data[total_points_col]
            ppg = player_data[ppg_col]
            output += f"{season_label}\t Points: {points} \t PPG: {ppg}\n"
    
    if not output:
        output = f"No data available for player: {playername}"
        
    print(output)


    #########################################

def store_historical_data(df_current, df_23_24, df_22_23, df_21_22, df_20_21, df_19_20):
    historical_data = [
        (df_23_24, "2023_24"),
        (df_22_23, "2022_23"),
        (df_21_22, "2021_22"),
        (df_20_21, "2020_21"),
        (df_19_20, "2019_20")
    ]
    
    for _, season_label in historical_data:
        df_current[f'total_points_{season_label}'] = None
        df_current[f'PPG_{season_label}'] = None

    for player in df_current['name']:
        for df, season_label in historical_data:
            try:
                player_data = df[df['name'] == player]
                if not player_data.empty:
                    df_current.loc[df_current['name'] == player, f'total_points_{season_label}'] = player_data['total_points'].values[0]
                    df_current.loc[df_current['name'] == player, f'PPG_{season_label}'] = player_data['points_per_game'].values[0]
            except Exception as e:
                print(f"Error processing player {player} for season {season_label}: {e}")

##################################################

def sort_out_columns(df):
    # Come back and make integers of all numerical columns
    df['points_per_game'] = df['points_per_game'].astype(float).round(2)
    df['now_cost'] = df['now_cost'].astype(float) / 10
    df['name'] = df['first_name'] + " " + df['second_name']
    df['ppg_per_euro'] = (df['points_per_game'] / df['now_cost']).round(3)
    return df
