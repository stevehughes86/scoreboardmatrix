#!/usr/bin/env python

from lxml import html
import requests

page = requests.get('https://www.totalcricketscorer.com/TCSLive/TCSClubScoresWidget.aspx?ctry=United+Kingdom&rgn=Wales&clb=Lisvane+CC')
tree = html.fromstring(page.content)

score1 = tree.xpath('//span[@id="lbl1stInn1"]/text()')
score2 = tree.xpath('//span[@id="lbl1stInn2"]/text()')

print 'Home ', score1
print 'Away ', score2