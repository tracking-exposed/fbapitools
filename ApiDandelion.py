# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:52:20 2018

@author: Fede
"""

import urllib3
import requests
import json
import os
import fb_scrape_public as fsp
import pandas

os.chdir("E:\ItaElectionFeeds\dandelion")

sourceslist = [,'liberieuguali2018','partitodemocratico.it','ForzaItaliaUfficiale','LegaNordUfficiale','casapounditalia','movimentocinquestelle']
postsIdslist = []
for source in sourceslist:
    outName = source + ".csv"
    if os.path.exists(outName):
        continue
    else:
        posts = fsp.scrape_fb(token="356213428133944|KlA5S4ouLF3QGC-0qNGFm_ZxqJc",ids= source, outfile= source + '.csv', end_date='2018-01-12')
        data = pandas.DataFrame(posts)
        postsIdslist.append(data[16])

commentslist = []
for idss in postsIdslist:
    for post in idss:
        print(post)
        destName = str(post) + ".csv"
        if os.path.exists(destName):
            continue
        else:
            data = fsp.scrape_fb("356213428133944","41c262db64ad42495efb33e754df5573",ids= post,scrape_mode="comments", outfile=destName) 
            df = pandas.DataFrame(data)
            sorteddata = df.sort_values([4], ascending=[False])
            comments = sorteddata[2][:9]
            commentslist.append(comments)


for piece in commentslist:
    print('sto analizzando:' + piece)
    f = urllib3.request.urlencode({"min_confidence" : "0.6", "text" : piece , "country" : "-1" , "social" : "False", "top_entities" : "8", "token": "9462a113d37b426496eb88ce3286ce8c" })
    print(f)
    f = requests.get(f)
    #import pdb; pdb.pset_trace()
    with open("284515247529_10155813499437530"+"comments" + ".json", 'w') as fp: 
        json.dump(f.json(), fp)
    
    







#https://api.dandelion.eu/datatxt/nex/v1/?min_confidence=0.6&url=https%3A%2F%2Ffacebook.tracking.exposed%2Finitiatives&country=-1&social=False&top_entities=8&token=9462a113d37b426496eb88ce3286ce8c