# -*- coding: utf-8 -*-
"""
~~~ create_from_result.py ~~~
Standard arg[1] -> arg[2] interface
This script takes an annotated docs as input,
it produced network result from it without sending city information

by Ruizhi 
April 2013 
"""
import sys
import re

class CityGraph(object):
    def __init__(self,files,silent = False):
        self.f0 = files[0]
        self.f1 = files[1]
        self.silent = silent

    def init(self):
    #build city count list on a doc base
        self.docNum = 0
        s = self.extractDoc()
        self.doc_dict = []
        while s != "":                        
            self.doc_dict.append({})
            self.update_dict(s)
            s = self.extractDoc()    

    def update_dict(self, docstr):
    #build the city count list for each doc
        p = re.compile(r'<NE:CITY.*?>.*?</NE:CITY>')
        list = p.findall(docstr)
        n = self.docNum - 1
        for items in list:
            name = items[items.find('>')+1:items.find('<',items.find('<')+1)]
            if self.doc_dict[n].has_key(name):
                self.doc_dict[n][name] += 1
            else:
                self.doc_dict[n][name] = 1


    def out_city_count_list(self):
    #write the city count list to output file
        self.f1.write("%20s %5s %5s\n"  %("CITY NAME", "DOC", "COUNT")) 
        i = 0
        for each_doc in self.doc_dict:
            i += 1
            if each_doc:
                for each_city in each_doc:
                    self.f1.write("%20s %5.0f %5.0f\n" %(each_city, i, each_doc[each_city]))              

    def extractDoc(self):
    #extract doc string from input file docly
        c = self.f0.readline()    
        s = ""
        while c and not "<doc>" in c:
            c = self.f0.readline()        
        if c:        
            c = self.f0.readline()
            while not "</doc>" in c:
                s += c
                c = self.f0.readline()        
            self.docNum += 1
        return s
            

def main(argv):
    f0 = open(argv[1], "r")
    f = open(argv[2], "w")
    doer = CityGraph([f0,f])
    doer.init()
    doer.out_city_count_list()
    f0.close()
    f.close()

if __name__ == "__main__":
    main(sys.argv)