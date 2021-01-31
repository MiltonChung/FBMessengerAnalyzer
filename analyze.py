import tkinter as tk
from tkinter import filedialog
import json
import os

directory = r""
namesDict = {}

def get_file_location():
  global directory
  directory = filedialog.askdirectory()
  lbl_file_location["text"] = directory
  print(directory)

def output_analyzed_files():
  print(directory)
  # Loop through each folder + file to initialize the Names Dictionary
  for filename in os.listdir(directory):
    subdir = os.path.join(directory, filename)
    # Each person's folder
    for personFolder in os.listdir(subdir):
      if personFolder.endswith('.json'):
        personJson = os.path.join(subdir, personFolder)
        initializeNames(personJson)
        
  # Loop through each folder + file to update dictionary values
  for filename in os.listdir(directory):
    subdir = os.path.join(directory, filename)
    # Each person's folder
    for personFolder in os.listdir(subdir):
      if personFolder.endswith('.json'):
        personJson = os.path.join(subdir, personFolder)
        openFiles(personJson)

  # Delete unclean data
  namesDict.pop('Facebook User')

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

def initializeNames(personJson):
	with open(personJson) as f:
		data = json.load(f)

	if len(data['participants']) == 2:
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


# Set-up the window
window = tk.Tk()
window.title("Messenger Analyzer")
window.resizable(width=True, height=True)
window.geometry('700x500')

# Program Title
frame_title = tk.Frame(master=window, height=150)
frame_title.pack(fill=tk.X)
title = tk.Label(text='Messenger Analyzer', master=frame_title, font=('Arial', 35), justify=tk.CENTER)
title.pack()

# Instructions
# frame_instr = tk.Frame(master=window, height=150)
# frame_instr.pack(fill=tk.X)
# instr = tk.Text( master=frame_instr, font=('Arial', 18))
# instr.insert(tk.INSERT, "asdasd")
# instr.insert(tk.END, 'asdad123123')
# instr.pack()

# File Location
btn_get_file = tk.Button(
  master=window,
  text="Select your foler",
  command=get_file_location
)
lbl_file_location = tk.Label(master=window, text="")
btn_get_file.pack()
lbl_file_location.pack()

# Analyze
btn_analyze = tk.Button(
  master=window,
  text="Analyze!",
  command=output_analyzed_files
)
btn_analyze.pack()

# Run the application
window.mainloop()