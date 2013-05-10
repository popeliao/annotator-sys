#To improve list
#1 filter list could be converted into lower case


# -*- coding: utf-8 -*-
"""
~~~ city_locater_in_ORG.py ~~~
Standard arg[1] -> arg[2] interface
Dependency: a pickle file named city_name.pickle

This script takes an NER-tool annotated docs as input,
it conducts post-process that locate all city name inside ORG annotations, 
and mark it as CITY. The eventual output is a post-processed doc

by Ruizhi 
April 2013 
"""

import sys
import re
import pickle

class City_locater_in_ORG(object):
    def __init__(self, city_name_list, fin, fout, silent = False):
        self.city_name_list = pickle.load(city_name_list)
        self.fin = fin
        self.fout = fout
        self.silent = silent #indicating whether will output a doc

    def readIn(self, s):
        if not self.silent:
            self.context = self.fin.read()  
        else:
            self.context = s    

    def process(self):
        #filter the input fin based on filterList        
        p = re.compile(r'<NE:ORG.*?>.*?</NE:ORG>')
        pmatch = re.compile(r'<NE:ORG.*?>(.*?)</NE:ORG>')
        tagList = p.findall(self.context)
        elseList = p.split(self.context)
        result = ''
        for i in range(len(tagList)):                        
            result += elseList[i]
            m = pmatch.match(tagList[i])
            tmp = self.isCityInside(m.group(1))
            result += tmp[0] if tmp[1] else tagList[i] 
            #will unmark ORG if CITY exsits inside
            
        if len(tagList) < len(elseList):
            result += elseList[-1]
        if not self.silent:
            self.fout.write(result)
        return result

    def isCityInside(self, str):
        #return result, flag
        #result is the processed string, 
        #flag indicates whether at least one city name found        
        #When matching city name, it is greedy and right-first
        result = ''        
        allWords = str.split()
        n = len(allWords)        
        begin = 0
        while begin < n:
            end = n
            while end > begin:
                if ' '.join(allWords[begin:end]).lower() in self.city_name_list:
                    result += '<NE:CITY>'+ ' '.join(allWords[begin:end]) +'</NE:CITY> '
                    if end == n:
                        return [result[:-1], True] #-1 to reduce the ending blank
                    else:
                        result += self.isCityInside(' '.join(allWords[end:]))[0]                    
                        return [result, True] 
                end -= 1
            result += allWords[begin] + ' '
            begin += 1
        return [result[:-1], False] #-1 to reduce the ending blank


def main(argv):
    f = open("city_name.pickle",'r') 	
    #filter.pickle is the pickle docs that store the filterList
    fin = open(argv[1],"r")
    fout = open(argv[2],"w")        
    doer = City_locater_in_ORG(f, fin, fout)
    doer.readIn(None)
    doer.process()    
    #Test cases
    #print doer.isCityInside("The National Council For Culture")[0]+'kk'
    #print doer.isCityInside("National University of Mexico")[0]+'kk'
    #print doer.isCityInside("Sharon Lockhart")[0]+'kk'
    fout.close()
    fin.close()
    f.close()


if __name__ == "__main__":
    main(sys.argv)
