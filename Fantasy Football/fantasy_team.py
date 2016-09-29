# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 22:40:12 2015

@author: shubham
"""

import requests, cPickle, shutil, time

all = {}
errorout = open('errors.log', 'w')  #Write all errors to this file

for i in range(1,679):
    playerurl = "http://fantasy.premierleague.com/web/api/elements/%s/"
    r = requests.get(playerurl % i)
    
    if r.status_code !=200: 
        continue
    if i%10 ==0:
        print i
        
    try:
        all[i] = r.json()
    except ValueError:
        print "Failed parsing player No. %s" % i
        errorout.write("Failed to parse player no. %s: %s\n" % (i, r.content))

cPickle.dump(all, outfile)        