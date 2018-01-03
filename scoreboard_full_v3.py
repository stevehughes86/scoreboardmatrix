#!/usr/bin/env python

#Import all needed repositories
from lxml import html
import requests

import time
from random import randrange

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

#######Create matrix device#######
#cascaded = number of matrices - doesnt work on laptop

#device = led.matrix(cascaded=2)
print('matrices created')
#device.flush()

switchToggle = 1

#weblink counter
w = 0

#######List of weblinks#######
weblink = [
'https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Wales&clb=Lisvane+CC',
'https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Wales&clb=Malpas+CC%2c+Wales',
'https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Oxfordshire&clb=Didcot',
'https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Oxfordshire&clb=Challow+and+Childrey'
]

#######Create functions#######

def scoredata(weblink):
	#get html from Lisvane CC TCS widget
	page = requests.get(weblink)#'https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Wales&clb=Lisvane+CC')
	tree = html.fromstring(page.content)

	#Get 3 letter team names home/away
	homeTeamGet = tree.xpath('//span[@id="lblTeam1"]/text()')
	awayTeamGet = tree.xpath('//span[@id="lblTeam2"]/text()')

	homeTeam = ''.join(homeTeamGet)
	awayTeam = ''.join(awayTeamGet)

	print('Home Team: ', homeTeam)
	print('Away Team: ', awayTeam)

	#find contents of 1st Inn spans
	score1 = tree.xpath('//span[@id="lbl1stInn1"]/text()')
	score2 = tree.xpath('//span[@id="lbl1stInn2"]/text()')
		
	homeScore = ''.join(score1)
	awayScore = ''.join(score2)

	#for testing purposes - can delete later
	print('Home ', homeScore)
	print('Away ', awayScore)

	#create counter
	i = 0
	j = 0

	#create lists
	homeScoreList = []
	awayScoreList = []
	homeWicketList = []
	awayWicketList = []

	#testing outputs - keep
	for letter in homeScore:
		if letter.isdigit():
			print(letter)
			i += 1
			homeScoreList.append(letter)
		else:
			print('This is not a digit')
			i +=1
			break

	#check score list population and length
	print('Score: ', homeScoreList, ': Digits: ', len(homeScoreList))

	#check score is 3 digits long, if not add 0s to the front
	while len(homeScoreList) < 3:
		homeScoreList.insert(0,'0')

	print('3 digit total: ', homeScoreList)

	#start reading wickets after -
	homeWicket = homeScore[i:]

	for letter in homeWicket:
		if letter.isdigit():
			print(letter)
			homeWicketList.append(letter)
		elif letter == 'a':	#Occasionally writen ao instead of 10
			homeWicketList.append('1')
			homeWicketList.append('0')
			break
		else:
			print('No more digits')
			break

	#check wicket list population - delete later
	print('Wickets: ', homeWicketList,': Digits: ', len(homeWicketList))

	while len(homeWicketList) < 2:
		homeWicketList.insert(0,'0')

	print('2 digits wickets: ', homeWicketList)

	print('Home Score: {} for {}'.format(''.join(homeScoreList), ''.join(homeWicketList)))

	#Repeat for away team
	for letter in awayScore:
		if letter.isdigit():
			j += 1
			awayScoreList.append(letter)
		else:
			j +=1
			break

	while len(awayScoreList) < 3:
		awayScoreList.insert(0,'0')

	awayWicket = awayScore[j:]

	for letter in awayWicket:
		if letter.isdigit():
			awayWicketList.append(letter)
		elif letter == 'a':	#Occasionally writen ao instead of 10
			awayWicketList.append('1')
			awayWicketList.append('0')
			break
		else:
			break

	while len(awayWicketList) < 2:
		awayWicketList.insert(0,'0')

	print('Away Score: {} for {}'.format(''.join(awayScoreList), ''.join(awayWicketList))) 

	#join lists together into one 10 character string
	scoreboardList = []
	scoreboardList = homeTeamGet + awayTeamGet + homeScoreList + homeWicketList + awayScoreList + awayWicketList
	
	#declare scoreboard as global variable
	global scoreboard
	
	scoreboard = ''.join(scoreboardList)	#Join the lists into a single string
	print('scoredata() scoreboard: ', scoreboard)

	return;

def showScore():
#	#Clear matrix from before
#	device.flush()
#
#	#Send scoreboard score to matrices
#	device.show_message(scoreboard, font=proportional(CP437_FONT))
	print('showing message')

#	#print scoreboard for testing
	print('showScore()= ', scoreboard)

	return;

#Create infinite loop
while True:

#Check switch position
##
##if switch Toggle code goes here
##

	#Check switch position
	while (switchToggle == 1):
		print('Switch up')

		scoredata(weblink[0])
		showScore()

		time.sleep(60)


	else:
		print('Switch down')

		if (w < len(weblink)):
			scoredata(weblink[w])
			showScore()

			time.sleep(10)
			
			w += 1
		
		else:
			w -= len(weblink)
