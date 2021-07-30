import time, urllib, json
from urllib.request import urlopen

def getInfo():

	##### MODIFY JUST IN THIS SECTION #####
	apiKey = 'yourAPIKey'
	channelId = 'yourChannelID'
	videoID = 'yourVideoID' ## you can get it from detaching the youtube live chat
	##### END OF CONFIGURATIONS #####
	
	try:
		
		urlCanal = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=' + channelId + '&key=' + apiKey
		urlVideo = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=' + videoID + '&key=' + apiKey
		responseCanal = urlopen(urlCanal).read().decode('utf-8')
		responseVideo = urlopen(urlVideo).read().decode('utf-8')
		dataCanal = json.loads(responseCanal)
		dataVideo = json.loads(responseVideo)
		
		## Dados do Canal
		if (dataCanal != ''):
			subs = dataCanal['items'][0]['statistics']['subscriberCount']
			print('Subs: ' + subs)
			f = open('subs.txt', 'w')
			f.write(subs)
			f.close()
		else:
			print("No data received, check your Channel ID")
		
		## Dados do Vídeo
		if (dataVideo != ''):
			views = dataVideo['items'][0]['statistics']['viewCount']
			print('Views: ' + views)
			fv = open('views.txt', 'w')
			fv.write(views)
			fv.close()
   
			likes = dataVideo['items'][0]['statistics']['likeCount']
			print('Likes: ' + likes)
			fl = open('likes.txt', 'w')
			fl.write(likes)
			fl.close()
   
		else:
			print("No data received, check your Channel ID")
		
	except:
		print("Something went wrong, check your API Key, Video ID and Channel ID!")
	
# END: def getInfo()

if __name__ == '__main__':
    while True:
        getInfo()
        # CUSTOM: Sleep for a number of seconds before checking again
        time.sleep(5)
# END: if __name__ == '__main__'