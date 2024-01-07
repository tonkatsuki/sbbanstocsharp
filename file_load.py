import json


def oldFileLoader(oldFile):
    with open(oldFile, "r") as oldBanData:
        oldBans = json.load(oldBanData)
        return oldBans
