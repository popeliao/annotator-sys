# -*- coding: utf-8 -*-
"""
~~~ extract_header_city.py ~~~
Standard argv[1]->argv[2] interfaces
Depedency: need raw_strategy package

This script takes an NER-tool annotated docs as input,
it conducts post-process indicated by the startegy mixer
The eventual output is a post-processed doc

by Ruizhi 
April 2013 
"""

import os
import sys
from raw_strategy import city_locater_in_ORG, filter_out, word_filter_out, city_locater_in_header

class Word_Filter(object):
    def __init__(self,fin, fout, silent = False):        
        self.fin = fin
        self.fout = fout
        self.silent = silent #indicating whether will output a doc

    def process(self):
        #filter the input fin based on filterList
        context = self.fin.read()   #use a sentinel for convenience 
        dat_city_list = open("raw_strategy/city_name.pickle",'r') 
        dat_filter_list = open("raw_strategy/filter_out.pickle",'r')   
        dat_word_filter_list = open("raw_strategy/word_filter_out.pickle",'r') 

        s1 = city_locater_in_ORG.City_locater_in_ORG(dat_city_list, None, None, True)
        s1.readIn(context)
        things = s1.process()   
        
        s2 = filter_out.Filter(dat_filter_list, None, None, True)
        s2.readIn(things) 
        things = s2.filter()

        s3 = word_filter_out.Word_Filter(dat_word_filter_list, None, None, True)
        s3.readIn(things) 
        things = s3.filter()    

        dat_city_list.close()
        dat_city_list = open("raw_strategy/city_name.pickle",'r') 
        s4 = city_locater_in_header.City_locater_in_header(dat_city_list, None, None, True)
        s4.readIn(things)
        things = s4.process()  

        dat_word_filter_list.close()
        dat_filter_list.close()
        dat_city_list.close()
        if not self.silent:
            self.fout.write(things)
        return things

def main(argv):    
    #filter.pickle is the pickle docs that store the filterList
    fin = open(argv[1],"r")
    fout = open(argv[2],"w")        
    doer = Word_Filter(fin, fout)
    doer.process()    
    fout.close()
    fin.close()

if __name__ == "__main__":
    main(sys.argv)
