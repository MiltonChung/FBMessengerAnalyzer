# Facebook Messenger Analyzer

Simple Facebook Messenger analyzer where it tells you who you have interacted with the most(excluding groupchats).

## Table of contents

-  [About](#about)
-  [Features](#features)
-  [Future Features](#future-features)
-  [Setup](#setup)
-  [Instructions](#instructions)
-  [Technologies](#technologies)
-  [Challenges](#challenges)
-  [Inspiration](#inspiration)
-  [Time Spent](#time-spent)
-  [Bugs](#bugs)

## About

This project was built using Python with the help of tkinter python GUI library for the user interface. The analysis can take anywhere from a few miliseconds to couple of seconds
depending on how much folders and data you have. Once the analysis is done, it will produce 3 files: MA_Alphabetical_Order.txt , MA_Chat_Count_Order.txt , and MA_Total_Count_Order.txt.
Each file contains JSON output of your data.
- MA_Alphabetical_Order.txt: Orders your output alphabetically
- MA_Chat_Count_Order.txt: Orders your output by only chat(pure messages without photos, stickers, etc...) count
- MA_Total_Count_Order.txt: Orders your output by all interactions(including chat, gifs, photos, etc...) count

## Features

-  Analyze user data and order them alphabetically, total, and chat

## Future Features

-  Have clear graphs(pandas and matplotlib) to visualize the data better
-  Most used words(with all friends and with each friend)
-  Sentiment analysis(nltk) 

## Setup

To run this project, download this MessengerAnalyzer.py(preferably put it in a folder) and double click it to run the GUI, and make sure you know where to find your facebook
messenger folder.

## Instructions

1. Go to your facebook "Settings"(top right drop-down menu) > "Your Facebook Information" > Download Your Information
2. Request the data in JSON format and any Media Quality. Go down a little and click Deselect All and check only the Messages checkbox and click Create File.
3. Wait until Facebook creates your data and download them(usually takes about half a day).
4. Combine all the messages folders together into one folder.
5. In the Messenger Analyzer program, select the /messages/inbox folder. Ex: C:\Users\Name\Desktop\messages\inbox. Make sure the inbox folder contains folders of your friends chat history.

## Technologies

Project is created with:

-  Python
-  tkinter Python GUI library

## Challenges

-  Finding the correct library/functions to loop through the folders of each person and reading/writing files
-  Python dictionary was kind of hard to work with at first(accessing values, ordering them, etc...)
-  First time using tkinter library

## Inspiration

On a Friday afternoon, I was wondering who I text the most on messenger and all the little statistics along with it. I decided to make this little program to analyze my messenger data.

## Time Spent

So far, I've spent around 9.5 hours on this project!

## Bugs

If you find any bugs or something isn't working, make an issue or contact me!
