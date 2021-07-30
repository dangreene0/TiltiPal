from tools.errorDefs import NoCampaignError, NoPreviousFileError
import json

def readHistory():
    with open('data/history.json') as f:
        data = json.load(f)
        try:
            previous = data["previousFile"]
        except Exception as e:
            raise NoPreviousFileError
        try:
            event = data["lastEvent"]
        except Exception as e:
            raise NoCampaignError
    return previous, event
 
                    