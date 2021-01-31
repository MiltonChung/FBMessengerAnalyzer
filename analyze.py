import tkinter as tk
from tkinter import filedialog
import json
import os

directory = r""
namesDict = {}
isComplete = False

############ FUNCTIONS ############
# Get the file location of the folder
def get_file_location():
  global directory
  directory = filedialog.askdirectory()
  lbl_file_location["text"] = directory
  print(directory)

# Display Loading... text and any error msg
def loading():
  # If user didn't select any folder
  if (directory == ''):
    lbl_loading['text'] = 'Please select a folder location'
  else:
    try:
      # Run this if the user selected the correct folder
      lbl_loading['text'] = 'Analyzing...                                       '
      lbl_complete['text'] = ''
      window.update_idletasks()
      output_analyzed_files()
    except:
      # If user selected the wrong folder
      lbl_loading['text'] = 'Sorry... Something went wrong! Maybe you selected the wrong foler'
    
# Run the analysis
def output_analyzed_files():
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
  lbl_loading['text'] = ''
  lbl_complete['text'] = 'Done! The files are in the same folder as this program.'

# Initialize the Names Dictionary
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


############ Tkinter Window Logic ############
# Set-up the window
window = tk.Tk()
window.title("Messenger Analyzer")
window.configure(bg='#fafafa')
window.resizable(width=True, height=True)
window.geometry('700x500')

# Program Title
frame_title = tk.Frame(master=window, height=150, bg='#fafafa')
frame_title.pack()
title = tk.Label(text='Messenger Analyzer', master=frame_title, font=("Helvetica", "35", "bold"),  bg='#fafafa')
title.pack()

# Instructions
# frame_instr = tk.Frame(master=window, height=150)
# frame_instr.pack(fill=tk.X)
# instr = tk.Text( master=frame_instr, font=('Arial', 18))
# instr.insert(tk.INSERT, "asdasd")
# instr.insert(tk.END, 'asdad123123')
# instr.pack()

# File Location
frame_file = tk.Frame(master=window, height= 150, bg='#fafafa')
frame_file.pack(side=tk.TOP)
btn_get_file = tk.Button(
  master=frame_file,
	font=("Helvetica",12),
  text="Select your foler",
  command=get_file_location,
	activebackground='#918cff',
	bg='#dad9ff',
	relief=tk.GROOVE
)
lbl_file_location = tk.Label(master=frame_file, text="", bg='#fafafa')
btn_get_file.pack(padx=5, pady=(60, 10), side=tk.LEFT)
lbl_file_location.pack( pady=(60, 10), side=tk.LEFT)

# Analyze Button
frame_analyze = tk.Frame(master=window, bg='#fafafa')
frame_analyze.pack(side=tk.TOP)
btn_analyze = tk.Button(
  master=frame_analyze,
  text="Analyze!",
  command=loading,
	font=("Helvetica", 30),
	activebackground='#918cff',
	bg='#dad9ff',
)
lbl_loading = tk.Label(master=frame_analyze, text="", bg='#fafafa', justify=tk.CENTER)
lbl_complete = tk.Label(master=frame_analyze, text="", bg='#fafafa', justify=tk.CENTER)
btn_analyze.pack(pady=(50, 10), side=tk.TOP)
lbl_loading.pack(pady=12, side=tk.LEFT)
lbl_complete.pack(pady=12, side=tk.LEFT)


# Run the application
window.mainloop()