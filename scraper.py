# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:05:34 2018

@author: Fede
"""
import pandas
import fb_scrape_public as fsp
import os
import json


filename='ItaSources.csv'
with open(filename, 'r') as f:
    for name in f:
        print(name)
        #f.replace('\n','')
        if pandas.Period('2018') is True :
            posts = fsp.scrape_fb(token="3csdcsdcc",ids= name[:-1], outfile= name[:-1] + '.csv')
        else:
