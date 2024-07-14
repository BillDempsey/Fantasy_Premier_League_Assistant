# Function to take user input which chooses the metric to sort by...
# ... the number of players to display this for...
# ... and calls the relevant function to do so.
def choose_metric(dataframe, league_teams):
    chosen_metric = input("Choose one of the following metrics to display:\ntotal_points\npoints_per_game\nPPGPE\nep_this\nep_next\n\n") # include try/catch for anything other than strings (already done in function? Better to do it here.)
    nplayers = int(input("\nChoose how many players you want displayed:\n\n"))  # Include try/catch for anything other than positive integers

    if chosen_metric == 'PPGPE':
        nplayers_PPGE(dataframe, nplayers, league_teams)
    elif chosen_metric == 'points_per_game':
        nplayers_PPG(dataframe, nplayers, league_teams)
    elif chosen_metric == 'total_points':
        nplayers_total_points(dataframe, nplayers, league_teams)
    elif chosen_metric == 'ep_this':
        nplayers_ep_this(dataframe, nplayers, league_teams)
    elif chosen_metric == 'ep_next':
        nplayers_ep_next(dataframe, nplayers, league_teams)
    else:
        print('Invalid output for "metric" field')  # Maybe swap this for an earlier try/catch

##################################################################################################################################
# All the functions which print out the n players leading the chosen metric

def nplayers_PPGE(dataframe, nplayers, league_teams):
    answer = int(input("\nWhat is the minimum number of points you want the players on display to have?\n\n"))
    ordered = dataframe.sort_values('ppg_per_euro', ascending=False)
    filtered = ordered[ordered['total_points'] > answer]
    top_n = filtered.head(nplayers)
    for i in top_n.index:
        playername = dataframe.loc[i, 'web_name']
        player_report(dataframe, playername, league_teams)

def nplayers_PPG(dataframe, nplayers, league_teams):
    top_n = dataframe.sort_values('points_per_game', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'web_name']
        player_report(dataframe, playername, league_teams)

def nplayers_total_points(dataframe, nplayers, league_teams):
    top_n = dataframe.sort_values('total_points', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'web_name']
        player_report(dataframe, playername, league_teams)

def nplayers_ep_this(dataframe, nplayers, league_teams):
    top_n = dataframe.sort_values('ep_this', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'web_name']
        player_report(dataframe, playername, league_teams)

def nplayers_ep_next(dataframe, nplayers, league_teams):
    top_n = dataframe.sort_values('ep_next', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'web_name']
        player_report(dataframe, playername, league_teams)


##################################################################################################################################
# Find a player by name in the dataframe and print out their data

def player_report(dataframe, webname, league_teams):
    # Include try/catch here, checking a) if the name exists b) if it's a duplicate
    # Maybe use combination of first and surnames instead in time

    # Set up a kind of fuzzy match to catch the names if spelled incorrectly. 
    # Also account for 2 similar/same names
    player = dataframe[dataframe['web_name'] == webname].iloc[0]
    position = {1: 'GK', 2: 'Def', 3: 'Mid', 4: 'Fwd'}

    #Change the %s to %d when converting the points to decimals later
    player_element_type = int(player['element_type'])
    player_team_index = int(player['team']) - 1
    print(" \n")
    print(f"Player:\t\t {player['web_name']}\n"
          f"Position:\t {position[player_element_type]}\n"
          f"Team:\t\t {league_teams[player_team_index]}\n"
          f"Points:\t\t {player['total_points']} \t\t\t({get_player_ranking(dataframe,'total_points', webname)})\n"
          f"Cost:\t\t {player['now_cost']:.1f} \t\t\t({get_player_ranking(dataframe,'now_cost', webname)})\n"
          f"PPG:\t\t {player['points_per_game']} \t\t\t({get_player_ranking(dataframe,'points_per_game', webname)})\n"
          f"PPGPE:\t\t {player['ppg_per_euro']:.3f} \t\t\t({get_player_ranking(dataframe,'ppg_per_euro', webname)})\n"
          f"EP this:\t {player['ep_this']} \t({player['chance_of_playing_this_round']}%) \t({get_player_ranking(dataframe,'ep_this', webname)})\n"
          f"EP next:\t {player['ep_next']} \t({player['chance_of_playing_next_round']}%) \t({get_player_ranking(dataframe,'ep_next', webname)})"
          )
    
    # Add in : \n PPG percentile %s\n PPGPE percentile %s\n
    # return player

#######################################################

# One function to order the players, called sort_by_chosen_metric(dataframe, metric)
# One called rank, called get_rank(dataframe, metric, webname)

def sort(dataframe, metric):
    sorted_df = dataframe.sort_values(metric, ascending=False)

    top_n = dataframe.sort_values('ep_this', ascending=False).head(nplayers)
    top_n_indices = top_n.index
    for i in top_n_indices:
        playername = dataframe.loc[i, 'web_name']

def get_player_ranking(dataframe, metric, webname):
    sorted_df = dataframe.sort_values(metric, ascending=False)
    # Reset the index of the sorted DataFrame so that the positions reflect the new order
    sorted_df.reset_index(drop=True, inplace=True)
    player_index = sorted_df[sorted_df['web_name'] == webname].index[0] # If indexError, name is probably incorrect PREVENT W/ T/C
    ranking = player_index + 1
    #print("Player ranking is ", ranking) # for debugging
    return ranking