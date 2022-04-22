from main import getPlayerCareer
import os

def test_getPlayerCareer():
    os.chdir("./project1_fastAPI_CI_apprunner/Get-player-s-career-data/playerdata_df/")
    assert "DataFrame" in str(type(getPlayerCareer("Kawhi Leonard")))
