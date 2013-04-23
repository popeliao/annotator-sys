# -*- coding: utf-8 -*-
"""
~~~ match_header.py ~~~
arg[1] arg[2]-> arg[3] interface
arg[1]: raw header
arg[2]: embedded annotated docs
arg[3]: associated header
axuilary: data_id_post.csv  ID mapping doc


by Ruizhi 
April 2013 
"""
import sys
import re
from map_id import Map_ID_Loader

class Header_Matcher(object):
    def __init__(self,files,silent = False):
        self.f1 = files[0]
        self.f2 = files[1]
        self.f3 = files[2]
        self.silent = silent
        f = open("data_id_post.csv","r")
        self.id_loader = Map_ID_Loader(f, True)
        self.id_dict = self.id_loader.getDict()
        f.close()

    def process(self):        
        self.make_annotated_dict()
        print len(self.annotated_dict)
        self.go_through_header_raw()
        print self.num

    def go_through_header_raw(self):        
        s, fid = self.extractDoc(self.f1)
        self.num = 0
        while s != "":                          
            if self.annotated_dict.has_key(fid):
                self.f3.write(s)
                self.num += 1                        
            s, fid = self.extractDoc(self.f1)  

    def make_annotated_dict(self):
        self.annotated_dict = {}
        s, fid = self.extractDoc(self.f2)
        while s != "":  
            self.annotated_dict[fid] = 1                        
            s, fid = self.extractDoc(self.f2)     

    def extractDoc(self, f):
    #extract doc string from input file docly
        c = f.readline()    
        s = ""
        fid = ""
        while c and not "<doc>" in c:
            c = f.readline()        
        if c:        
            c = f.readline()
            tmp = c.replace('<','').replace('>','')
            tmp = tmp.split()[0][:-1]           # <http:url\>:
            if self.id_dict.has_key(tmp):
                fid = self.id_dict[tmp]              
            while not "</doc>" in c:
                s += c
                c = f.readline()                    
        return s, fid
            

def main(argv):
    f1 = open(argv[1], "r")
    f2 = open(argv[2], "r")
    f3 = open(argv[3], "w")
    doer = Header_Matcher([f1,f2,f3])
    doer.process()
    f1.close()
    f2.close()
    f3.close()

if __name__ == "__main__":
    main(sys.argv)