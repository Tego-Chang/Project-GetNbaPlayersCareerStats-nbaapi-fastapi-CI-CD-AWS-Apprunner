from main import getPlayerCareer
import os

def test_getPlayerCareer():
    os.chdir("./project1_nba/Get-player-s-career-data")
    assert "DataFrame" in str(type(getPlayerCareer("Kawhi Leonard")))
