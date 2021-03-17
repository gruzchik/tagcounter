#!/usr/bin/python

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
#        print("number", counter)
#        for attr in attrs:
#            print("     attr:", attr)

#    def handle_endtag(self, tag):
#        print("End tag  :", tag)

#    def handle_data(self, data):
#        print("Data     :", data)

#    def handle_comment(self, data):
#        print("Comment  :", data)
#
#    def handle_entityref(self, name):
#        c = unichr(name2codepoint[name])
#        print("Named ent:", c)

#    def handle_charref(self, name):
#        if name.startswith('x'):
#            c = unichr(int(name[1:], 16))
#        else:
#            c = unichr(int(name))
#        print("Num ent  :", c)

#def handle_decl(self, data):
#    print("Decl     :", data)

parser = MyHTMLParser()


print("URL inside:", sys.argv[1])
r = requests.get(tagurl)
info = r.text
#info = '<html><head><title>Test</title></head>''<body><h1>Parse me!</h1><p><br><br></p><p>324324</p><p>ddd</p></body></html>'
print(info)
#print massive
parser.feed(info)
countlist = dict(Counter(listing))
print('countlist:', countlist)
#print('list', listing)
#pandalist = pd.Series(list).value_counts()
pandalist = countlist#.count()
print("\npandalist:\n", pandalist)
