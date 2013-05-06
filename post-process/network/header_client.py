# -*- coding: utf-8 -*-
"""
~~~ header_client.py ~~~
Standard arg[1] -> arg[2] interface
This script takes an annotated header file as input, 

by Ruizhi 
April 2013 
"""
import sys
import re
from map_id import Map_ID_Loader

class CityGraph_header(object):
    def __init__(self,files,silent = False):
        self.f0 = files[0]
        self.f1 = files[1]
        self.silent = silent
        f = open("data_id_post.csv","r")
        self.id_loader = Map_ID_Loader(f, True)
        self.id_dict = self.id_loader.getDict()
        f.close()

    def process(self):
        pdoc = re.compile(r'<doc>.*?</doc>', re.S)            
        docs = pdoc.findall(self.f0.read())                
        pcname = re.compile(r'<cname>.*?</cname>', re.S)        
        phead = re.compile(r'<head>.*?</head>', re.S)        
        pcity = re.compile(r'<NE:CITY.*?>.*?</NE:CITY>', re.S)
        i = 0

        for doc in docs:            
            i += 1
            client = ""
            strcname = pcname.findall(doc)[0]
            strhead = phead.findall(doc)[0]
            cities = pcity.findall(strcname)
            if cities:
                t = cities[0]
                client = t[t.find('>')+1:t.find('<',t.find('<')+1)]
            citycount = {}
            cities = pcity.findall(strhead)
            for items in cities:
                name = items[items.find('>')+1:items.find('<',items.find('<')+1)]
                if citycount.has_key(name):
                    citycount[name] += 1
                else:
                    citycount[name] = 1
            if not client and citycount:
                client = self.find_most(citycount)
            self.output(client, citycount, i)            

    def output(self, client, citycount, ith):
        self.f1.write("--------------------------------------\n")
        self.f1.write("header doc %5d\n" %(ith))
        if not client:
            client = "N/A"
        self.f1.write("client city is %20s\n" %(client))
        for k in citycount.keys():
            self.f1.write("%20s %5s\n"  %(k, citycount[k]))         

    def find_most(self,citycount):
        max = 0
        result = ''
        for k in citycount.keys():
            if citycount[k] > max:
                max = citycount[k]
                result = k
        return result

def main(argv):
    f0 = open(argv[1], "r")
    f = open(argv[2], "w")
    doer = CityGraph_header([f0,f])
    doer.process()
    f0.close()
    f.close()

if __name__ == "__main__":
    main(sys.argv)