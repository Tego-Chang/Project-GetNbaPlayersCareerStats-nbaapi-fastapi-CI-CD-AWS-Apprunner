from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
# import os


if __name__ == '__main__':
    # os.chdir("./project1_nba/Get-player-s-career-data")

    player_dict = players.get_players()
    active_player_dict = [player for player in player_dict if player['is_active'] == True]

    for player in active_player_dict:
        # print ("Downloading player data: " + player['full_name'])
        career = playercareerstats.PlayerCareerStats(player_id=player['id'])
        career.get_data_frames()[0].to_csv("./playerdata_df/" + player['full_name'] + ".csv")
        pass