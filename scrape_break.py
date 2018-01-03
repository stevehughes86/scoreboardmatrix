#!/usr/bin/env python

from lxml import html
import requests

page = requests.get('https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Wales&clb=Lisvane+CC')
tree = html.fromstring(page.content)

score1 = tree.xpath('//span[@id="lbl1stInn1"]/text()')
score2 = tree.xpath('//span[@id="lbl1stInn2"]/text()')

print 'Home ', score1
print 'Away ', score2

homeBracket = str(score1)
awayBracket = str(score2)

homeScore = homeBracket[2:]

print homeScore

i = 0

homeScoreList = []

print 'Score: '

for letter in homeScore:
	if letter.isdigit():
		print letter
		i += 1
		my_list.append(letter)
	else:
		print ("This is not a digit")
		i +=1
		break

print homeScoreList

print 'Wickets: '

homeWicket = homeScore[i:]

for letter in homeWicket:
	if letter.isdigit():
		print letter
		i +=1
	else:
		print ("No more digits")
		break