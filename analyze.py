import json
import os

directory = r"C:\Users\Mewton\Desktop\messenger\messages\inbox"
namesDict = {}

def initializeNames(personJson):
	with open(personJson) as f:
		data = json.load(f)

	if len(data['participants']) == 2:
		# print(data['participants'][0]['name'])
		participantName = data['participants'][0]['name']
		namesDict[participantName] = {
			'chat': 0,
			'gifs': 0,
			'photos': 0,
			'sticker': 0,
			'videos': 0,
			'files': 0,
			'audio_files': 0,
			'total': 0,
		}
		# print(json.dumps(namesDict, indent=4, sort_keys=True))

	f.close()

# Creates each person dictionary and add the count of all interactions
def openFiles(personJson):
	with open(personJson) as f:
		data = json.load(f)

	if len(data['participants']) == 2:
		name = data['participants'][0]['name']
		for message in data['messages']:
			if 'content' in message:
				namesDict[name]['chat'] = namesDict[name]['chat'] + 1
			elif 'gifs' in message:
				namesDict[name]['gifs'] = namesDict[name]['gifs'] + 1
			elif 'photos' in message:
				namesDict[name]['photos'] = namesDict[name]['photos'] + 1
			elif 'sticker' in message:
				namesDict[name]['sticker'] = namesDict[name]['sticker'] + 1
			elif 'videos' in message:
				namesDict[name]['videos'] = namesDict[name]['videos'] + 1
			elif 'files' in message:
				namesDict[name]['files'] = namesDict[name]['files'] + 1
			elif 'audio_files' in message:
				namesDict[name]['audio_files'] = namesDict[name]['audio_files'] + 1

	f.close()

# Loop through each folder + file 
# Inbox
for filename in os.listdir(directory):
	subdir = os.path.join(directory, filename)
	# Each person's folder
	for personFolder in os.listdir(subdir):
		if personFolder.endswith('.json'):
			personJson = os.path.join(subdir, personFolder)
			initializeNames(personJson)

statsFile = open('./messengertests.txt', 'w')
statsFile.write(json.dumps(namesDict, indent=4, sort_keys=True))
statsFile.close()
			
for filename in os.listdir(directory):
	subdir = os.path.join(directory, filename)
	# Each person's folder
	for personFolder in os.listdir(subdir):
		if personFolder.endswith('.json'):
			personJson = os.path.join(subdir, personFolder)
			openFiles(personJson)

# Delete unclean data
namesDict.pop('Facebook User')
# print(json.dumps(namesDict, indent=4, sort_keys=True))

# Count the total for each person (chat + gifs + photos + sticker + ...)
for personName in namesDict:
	for individualStat in namesDict[personName]:
		if individualStat != 'total':
			namesDict[personName]['total'] += namesDict[personName][individualStat]

# Order Alphabetically
statsFile = open('./messengerStatsUnordered.txt', 'w')
statsFile.write(json.dumps(namesDict, indent=4, sort_keys=True))
statsFile.close()

# Order by Chat count
statsFile = open('./messengerStatsChatOrder.txt', 'w')
chatOrderDict = dict(sorted(namesDict.items(), key=lambda item: item[1]['chat'], reverse = True))
statsFile.write(json.dumps(chatOrderDict, indent=4))
statsFile.close()

# Order by Total count
statsFile = open('./messengerStatsTotalOrder.txt', 'w')
totalOrderDict = dict(sorted(namesDict.items(), key=lambda item: item[1]['total'], reverse = True))
statsFile.write(json.dumps(totalOrderDict, indent=4))
statsFile.close()

print('Done!')
