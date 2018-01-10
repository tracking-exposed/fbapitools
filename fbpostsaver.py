#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:05:34 2018

@author: Fede
"""
import scrape_fb
import os
import json
import sys
import datetime
import pprint

keyfile = 'config/key.json'
destdirectory = 'collected'

if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    print("Using as source list: %s" % sys.argv[1])
else:
    print("Necessary source list as first argument")
    sys.exit(1)

if not os.path.isdir(destdirectory):
    print("Require '%s' destinastion directory: not found" % destdirectory)
    sys.exit(1)


today = datetime.date.today()
todayposts = os.path.join(destdirectory, today.strftime("%Y-%m-%d"))

try:
    os.mkdir(todayposts)
    print("Created '%s' directory to store today's results" % todayposts)
except FileExistsError:
    pass


with open(keyfile, 'r') as kf:
    key = json.load(kf)['key']

    with open(sys.argv[1], 'r', encoding='utf-8') as sourcesfp:
        sources = json.load(sourcesfp)
        """
        p sources[0]
        {'selezionato': False, 'orientamento': 'Destra', 'nome': 'Forza Italia News', 'pagina': 'https://www.facebook.com/forzaitalianews', 'tipo': 'Partito'}
        """

        for source in sources:
            pprint.pprint(source)
            if(source['pagina'].endswith('/')):
                print("Error in the object %s, %s ends with '/', clean it (skipped)" % (source['nome'], source['pagina']))
                continue

            pageName = source['pagina'].split('/')[-1]
            CSVoutput = os.path.join(todayposts, pageName + '.csv')
            JSONoutput = os.path.join(todayposts, pageName + '.json')
            print("Processing %s (%s output CSV file)" % (source['nome'], CSVoutput))
            if(os.path.exists(CSVoutput)):
                print("output file already exists: skipping")
                continue

            json_posts = scrape_fb.scrape_fb(token=key,ids=pageName, outfile=CSVoutput, end_date="2018-01-01")

            with open(JSONoutput, 'w+', encoding='utf-8') as jop:
                json.dump(json_posts, jop, sort_keys=True, indent=3)
                print("Saved JSONfile %s" % JSONoutput)

