#!/usr/bin/python

"""
Script for parsing of html tags
"""

import sys
from collections import Counter
import pandas as pd
import requests

print(len(sys.argv))
if (len(sys.argv)==2) or (len(sys.argv)==3):
    print('good')
    print("number of arguments is:", len(sys.argv)-1)
else:
    print('bad')
    print("number of arguments is:", len(sys.argv)-1)
    sys.exit(1)

counter = 0
listing =[]
existing_tag = False
tagurl = sys.argv[1]
print("URL outside", tagurl)

from html.parser import HTMLParser
#from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global counter, tagurl
        #print("Start tag:", tag)
        listing.append(tag)

        counter += 1

parser = MyHTMLParser()

print("URL inside:", sys.argv[1])
r = requests.get(tagurl)
info = r.text
print(info)
parser.feed(info)
print("\ncounter = "+str(counter))
countlist = dict(Counter(listing))

if (len(sys.argv)==3):
    for element in countlist:
        if element == sys.argv[2]:
            print("number of tag \""+str(sys.argv[2])+"\" =  "+str(countlist[sys.argv[2]]))
            existing_tag = True
    if existing_tag != True:
        print("the tag \""+str(sys.argv[2])+"\" does not exists in website\n")
print('countlist:', countlist)
#pandalist = pd.Series(list).value_counts()
pandalist = countlist#.count()
print("\npandalist:\n", pandalist)
