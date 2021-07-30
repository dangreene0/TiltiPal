import json
import requests

def main():
    ask = input("would you like to view a campaign\'s data?\n")
    if "y" in ask:
        with open('test.json') as f:
            data = json.load(f)
            for campaign in data:
                print(campaign)
                eventAsk = input(f"would you like to view {campaign}?\n")
                if "y" in eventAsk:
                    print(f"event is: {campaign}")
                    for info in data[campaign]:
                        eventCode = info['event-code']
                        userCode = info['user']
                        print(userCode, eventCode)
                        urlGen = f"https://tiltify.com/api/v3/users/{userCode}/campaigns/{eventCode}"
                        print(urlGen)
                        response = requests.get(urlGen)
                        tiltifyData = json.loads(response.text)
                        print(tiltifyData)
                    break
                    
                if "n" in eventAsk:
                    continue
        saveData = input("would you like to save your data?\n")
        if "y" in saveData:
            with open('empty.json', 'w') as f:
                json.dump(data, f, indent = 2)
    if "n" in ask:
        print('okei bye')
    
main()