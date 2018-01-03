#!/usr/bin/env python

#Import all needed repositories
from lxml import html
import requests

import time
from random import randrange

import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

startTime = time.time()

#Create matrix device - cascaded = number of matrices - doesnt work on laptop
#device = led.matrix(cascaded=1)
print 'matrices created'
#device.flush()

#Create infinite loop
while True:
	if ((time.time() - startTime) <= 60):	#Refresh score every minute
		time.sleep(1)

	else:
		#get html from Lisvane CC TCS widget
		page = requests.get('https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Wales&clb=Lisvane+CC')
		tree = html.fromstring(page.content)

		#Get 3 letter team names home/away
		homeTeamGet = tree.xpath('//span[@id="lblTeam1"]/text()')
		awayTeamGet = tree.xpath('//span[@id="lblTeam2"]/text()')

		homeTeam = ''.join(homeTeamGet)
		awayTeam = ''.join(awayTeamGet)

		print 'Home Team: ', homeTeam
		print 'Away Team: ', awayTeam

		#find contents of 1st Inn spans
		score1 = tree.xpath('//span[@id="lbl1stInn1"]/text()')
		score2 = tree.xpath('//span[@id="lbl1stInn2"]/text()')
		 
		#for testing purposes - can delete later
		print 'Home ', score1
		print 'Away ', score2

		#convert to string
		homeBracket = str(score1)
		awayBracket = str(score2)

		#ignore starting ['
		homeScore = homeBracket[2:]
		awayScore = awayBracket[2:]

		#testing purposes - can delete later
		print homeScore

		#create counter
		i = 0
		j = 0

		#create lists
		homeScoreList = []
		awayScoreList = []
		homeWicketList = []
		awayWicketList = []

		#testing outputs - keep
		print 'Score: '

		for letter in homeScore:
			if letter.isdigit():
				print letter
				i += 1
				homeScoreList.append(letter)
			else:
				print ("This is not a digit")
				i +=1
				break

		#check score list population and length
		print homeScoreList
		print len(homeScoreList)

		#check score is 3 digits long, if not add 0s to the front
		while len(homeScoreList) < 3:
			homeScoreList.insert(0,'0')

		print homeScoreList

		#start reading wickets after -
		homeWicket = homeScore[i:]

		print 'Wickets: '

		for letter in homeWicket:
			if letter.isdigit():
				print letter
				homeWicketList.append(letter)
			elif letter == 'a':	#Occasionally writen ao instead of 10
				homeWicketList.append('10')
				break
			else:
				print ("No more digits")
				break

		#check wicket list population - delete later
		print homeWicketList
		print len(homeWicketList)

		while len(homeWicketList) < 2:
			homeWicketList.insert(0,'0')

		print homeWicketList

		print 'Home Score: {} for {}'.format(homeScoreList, homeWicketList)

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
				awayWicketList.append('10')
				break
			else:
				break

		print 'Away Score: {} for {}'.format(awayScoreList, awayWicketList) 

		#join lists together into one 10 character string
		scoreboardList = []
		scoreboardList = homeScoreList + homeWicketList + awayScoreList + awayWicketList
		scoreboard = ''.join(scoreboardList)	#Join the lists into a single string
		print scoreboard

		#Clear matrix from before
#		device.flush()
#
#		#Send scoreboard score to matrices
#		device.show_message(scoreboard, font=proportional(CP437_FONT))
#		print "showing message"
#
#		#test hold for x time - doesnt work on laptop
#		s = '1'
#		device.show_message(s)
#
#		startTime = time.time()
#
#		time.sleep(50)

