from main import getPlayerCareer
import os

def test_getPlayerCareer():
    os.chdir("./playerdata_df/")
    assert "DataFrame" in str(type(getPlayerCareer("Kawhi Leonard")))
