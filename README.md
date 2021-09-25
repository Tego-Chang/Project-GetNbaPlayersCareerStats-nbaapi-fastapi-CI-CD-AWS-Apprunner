[![CI (Python application test with Github Actions)](https://github.com/Tego-Chang/Get-player-s-career-data/actions/workflows/main.yml/badge.svg)](https://github.com/Tego-Chang/Get-player-s-career-data/actions/workflows/main.yml)


# Get-player-s-career-data

The project is to demonstrate a basketball data querying service on AWS with implementation of CI and CD. 

- fetchNbaData.py: get the latest NBA data from nba website through nba_api (Author: Swar Patel https://github.com/swar).
- main.py: based on the collected data to realize providing the queried NBA player's accumulated career statistics. 
- playerdata_df: a directory stores all the active players' data in csv through nba_api.
- htmlDirectory: a directory stores the html of the table of the player being queried. 

Note: Due to NBA website blocks the request from AWS and Github (https://github.com/swar/nba_api/issues/155), we will not be able to utilize the Github Action's ability to automatically update the latest NBA data everytime code update is pushed. 
