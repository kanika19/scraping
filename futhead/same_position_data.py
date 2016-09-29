# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 16:40:31 2016

@author: Shubham
"""

import urllib2
from bs4 import BeautifulSoup
import pickle


BASE_URL= 'http://www.futhead.com/16/players/23095/mesut-ozil/similar/?by=position&page='

links = {}

def page_links(page_no):
    url = BASE_URL + str(page_no+1)
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    
    #Get grid of all players on the page    
    grid = soup.findAll('div', {'class':'player-page-listing'})[0]
    
    players = grid.findAll('a', {'class': 'hvr-grow margin-10'})
    
    for player in players:
        pname = player.find('div', {'class': 'playercard-name'}).string.lower()
        plink = 'http://www.futhead.com' + player['href']
        
        links[pname] = plink
        
        print pname, 'successfully stored in database'
    
#for i in range(30):
#    page_links(i)
#    
#    
    
    
    
    

fav = pickle.load( open( "links.json", "rb" ) )    
    
#    
#ovr = int(soup.find('div', {'class': 'playercard-rating'}).string)    
#pace = int(soup.find('div', {'class': 'playercard-attr playercard-attr1'}).text.split()[0])
#shoot = int(soup.find('div', {'class': 'playercard-attr playercard-attr2'}).text.split()[0])
#
#    
    
    
    
    
    