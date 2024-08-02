# Function to take user input which chooses the metric to sort by...
# ... the number of players to display this for...
# ... and calls the relevant function to do so.

def choose_metric(dataframe):
    chosen_metric = input("Choose one of the following metrics to display:\ntotal_points\npoints_per_game\nPPGPE\nep_this\nep_next\n\n") # include try/catch for anything other than strings (already done in function? Better to do it here.)
    nplayers = int(input("\nChoose how many players you want displayed:\n\n"))  # Include try/catch for anything other than positive integers

    if chosen_metric == 'PPGPE':
        nplayers_PPGE(dataframe, nplayers)
    elif chosen_metric == 'points_per_game':
        nplayers_PPG(dataframe, nplayers)
    elif chosen_metric == 'total_points':
        nplayers_total_points(dataframe, nplayers)
    elif chosen_metric == 'ep_this':
        nplayers_ep_this(dataframe, nplayers)
    elif chosen_metric == 'ep_next':
        nplayers_ep_next(dataframe, nplayers)
    else:
        print('Invalid output for "metric" field')  # Maybe swap this for an earlier try/catch

##################################################################################################################################
# All the functions which print out the n players leading the chosen metric

def nplayers_PPGE(dataframe, nplayers):
    answer = int(input("\nWhat is the minimum number of points you want the players on display to have?\n\n"))
    ordered = dataframe.sort_values('ppg_per_euro', ascending=False)
    filtered = ordered[ordered['total_points'] > answer]
    top_n = filtered.head(nplayers)
    for i in top_n.index:
        playername = dataframe.loc[i, 'name']
        player_report(dataframe, playername)

def nplayers_PPG(dataframe, nplayers):
    top_n = dataframe.sort_values('points_per_game', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(dataframe, playername)

def nplayers_total_points(dataframe, nplayers):
    top_n = dataframe.sort_values('total_points', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(dataframe, playername)

def nplayers_ep_this(dataframe, nplayers):
    top_n = dataframe.sort_values('ep_this', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(dataframe, playername)

def nplayers_ep_next(dataframe, nplayers):
    top_n = dataframe.sort_values('ep_next', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'name']
        player_report(dataframe, playername)


##################################################################################################################################
# Find a player by name in the dataframe and print out their data

def player_report(dataframe, playername):
    # Include try/catch here, checking a) if the name exists b) if it's a duplicate
    # Maybe use combination of first and surnames instead in time

    # Set up a kind of fuzzy match to catch the names if spelled incorrectly. 
    # Also account for 2 similar/same names
    player = dataframe[dataframe['name'] == playername].iloc[0]
    position = {1: 'GK', 2: 'Def', 3: 'Mid', 4: 'Fwd'}
    
    #Change the %s to %d when converting the points to decimals later
    player_element_type = int(player['element_type'])
    print(" \n")
    print(f"Player:\t\t {player['name']}\n"
          f"Position:\t {position[player_element_type]}\n"
          f"Points:\t\t {player['total_points']} \t\t\t({get_player_ranking(dataframe,'total_points', playername)})\n"
          f"Cost:\t\t {player['now_cost']:.1f} \t\t\t({get_player_ranking(dataframe,'now_cost', playername)})\n"
          f"PPG:\t\t {player['points_per_game']} \t\t\t({get_player_ranking(dataframe,'points_per_game', playername)})\n"
          f"PPGPE:\t\t {player['ppg_per_euro']:.3f} \t\t\t({get_player_ranking(dataframe,'ppg_per_euro', playername)})\n"
          f"EP this:\t {player['ep_this']} \t({player['chance_of_playing_this_round']}%) \t({get_player_ranking(dataframe,'ep_this', playername)})\n"
          f"EP next:\t {player['ep_next']} \t({player['chance_of_playing_next_round']}%) \t({get_player_ranking(dataframe,'ep_next', playername)})"
          )
    
    # Add in : \n PPG percentile %s\n PPGPE percentile %s\n
    # return player

#######################################################

def get_player_ranking(dataframe, metric, playername):
    sorted_df = dataframe.sort_values(metric, ascending=False)
    sorted_df.reset_index(drop=True, inplace=True) # Reset the index of the sorted DataFrame so that the positions reflect the new order
    player_index = sorted_df[sorted_df['name'] == playername].index[0] # If indexError, name is probably incorrect PREVENT W/ T/C
    ranking = player_index + 1
    return ranking

##########################################################
##################################################################################################################################

def get_historical_data_strings(playername, df_23_24, df_22_23, df_21_22, df_20_21, df_19_20):
    def get_player_data(playername, df, season):
        try:
            player_row = df[df['name'] == playername]
            if not player_row.empty:
                return player_row.iloc[0]
            else:
                return None
        except Exception:
            print(f"The name {playername} could not be found for the {season} season")
            return None

    playerdata_23_24 = get_player_data(playername, df_23_24, season="2023/24")
    playerdata_22_23 = get_player_data(playername, df_22_23, season="2022/23")
    playerdata_21_22 = get_player_data(playername, df_21_22, season="2021/22")
    playerdata_20_21 = get_player_data(playername, df_20_21, season="2020/21")
    playerdata_19_20 = get_player_data(playername, df_19_20, season="2019/20")

    output_1 = ""
    if playerdata_23_24 is not None:
        output_1 += f"2023/24\t Points: {playerdata_23_24['total_points']} \t PPG: {playerdata_23_24['points_per_game']}\n"
    if playerdata_22_23 is not None:
        output_1 += f"2022/23\t Points: {playerdata_22_23['total_points']} \t PPG: {playerdata_22_23['points_per_game']}\n"
    if playerdata_21_22 is not None:
        output_1 += f"2021/22\t Points: {playerdata_21_22['total_points']} \t PPG: {playerdata_21_22['points_per_game']}\n"
    if playerdata_20_21 is not None:
        output_1 += f"2020/21\t Points: {playerdata_20_21['total_points']} \t PPG: {playerdata_20_21['points_per_game']}\n"
    if playerdata_19_20 is not None:
        output_1 += f"2019/20\t Points: {playerdata_19_20['total_points']} \t PPG: {playerdata_19_20['points_per_game']}\n"

    if output_1 == "":
        output_1 = f"No data available for player: {playername}"
        
    print(output_1)