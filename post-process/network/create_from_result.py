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
from map_id import Map_ID_Loader

class CityGraph(object):
    def __init__(self,files,silent = False):
        self.f0 = files[0]
        self.f1 = files[1]
        self.silent = silent
        f = open("data_id_post.csv","r")
        self.id_loader = Map_ID_Loader(f, True)
        self.id_dict = self.id_loader.getDict()
        f.close()


    def init(self):
    #build city count list on a doc base
        self.docNum = 0
        s, fid = self.extractDoc()
        self.doc_dict = {}
        while s != "":                        
            self.doc_dict[fid] = {}
            self.update_dict(s, fid)
            s, fid = self.extractDoc()   

    def update_dict(self, docstr, fid):
    #build the city count list for each doc
        p = re.compile(r'<NE:CITY.*?>.*?</NE:CITY>')
        list = p.findall(docstr)        
        for items in list:
            name = items[items.find('>')+1:items.find('<',items.find('<')+1)]
            if self.doc_dict[fid].has_key(name):
                self.doc_dict[fid][name] += 1
            else:
                self.doc_dict[fid][name] = 1


    def out_city_count_list(self):
    #write the city count list to output file
        self.f1.write("%20s %20s %5s\n"  %("CITY NAME", "DOC", "COUNT"))         
        for doc_id in self.doc_dict: 
            if self.doc_dict[doc_id]:
                for each_city in self.doc_dict[doc_id]:
                    self.f1.write("%20s %20s %5.0f\n" %(each_city, doc_id, self.doc_dict[doc_id][each_city]))              

    def extractDoc(self):
    #extract doc string from input file docly
        c = self.f0.readline()    
        s = ""
        fid = ""
        while c and not "<doc>" in c:
            c = self.f0.readline()        
        if c:        
            c = self.f0.readline()
            fid = self.id_dict[c.split()[0][:-1]]    # all http url is directly followed <doc> and has a extra ':' at the end
            while not "</doc>" in c:
                s += c
                c = self.f0.readline()        
            self.docNum += 1
        return s, fid
            

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