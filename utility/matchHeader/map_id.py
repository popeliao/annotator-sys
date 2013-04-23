# -*- coding: utf-8 -*-
"""
~~~ map_id.py ~~~
use csv documents to map http url to a identical id

This script takes a csv docs as input,
it produce a python dict data type variable to represent the mapping

by Ruizhi 
April 2013 
"""
import sys
import re

class Map_ID_Loader(object):
    def __init__(self,fin = open("data_id_post.csv","r"),silent = True):
        self.fin = fin        
        self.silent = silent
        self.dict = {}
        self.load()

    def load(self):
    #load the dict from csv
        for line in self.fin:
            item = line.split(',')
            self.dict[item[1][:-1]] = item[0]   #-1 to delete the \n at the end

    def getDict(self):
        if not self.silent:
            print self.dict
        return self.dict

def main(argv):    
    if argv[0] == 1:
        f = open(argv[1], "r")    
    else:
        f = open("data_id_post.csv","r")
    doer = Map_ID_Loader(f, False)
    doer.getDict()
    f.close()

if __name__ == "__main__":
    main(sys.argv)