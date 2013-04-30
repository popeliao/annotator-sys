#To improve list
#1 filter list could be converted into lower case


# -*- coding: utf-8 -*-
"""
~~~ word_filter_out.py ~~~
Standard argv[1]->argv[2] interfaces
Depedency: a pickle file named word_filter_out.pickle

This script takes an NER-tool annotated docs as input,
it conducts post-process that filter all the words annotated as CITY 
when part of the word appears in the filter list. 

The eventual output is a post-processed doc

by Ruizhi 
April 2013 
"""


import sys
import re
import pickle

def compact_string_list(words, begin, end):
    s = ''
    for item in words[begin:end]:
        s += item + ' '
    return s[:-1]

def all_sub(s):
    words = s.split()
    k = len(words)
    result = []
    for start in range(k):
        for lent in range(k-start):
            result.append(compact_string_list(words, start, start+lent+1))
    return result

class Filter(object):
    def __init__(self,filterListPickle, fin, fout, silent = False):
        self.filterList = pickle.load(filterListPickle)
        self.fin = fin
        self.fout = fout
        self.silent = silent #indicating whether will output a doc

    def filter(self):
        #filter the input fin based on filterList
        context = self.fin.read()   #use a sentinel for convenience 
        p = re.compile(r'<NE:CITY.*?>.*?</NE:CITY>')
        pmatch = re.compile(r'<NE:CITY.*?>(.*?)</NE:CITY>')
        tagList = p.findall(context)
        elseList = p.split(context)
        result = ''
        for i in range(len(tagList)):                        
            result += elseList[i]
            m = pmatch.match(tagList[i])
            if any(item.lower() in self.filterList for item in all_sub(m.group(1))):
                result += m.group(1)                
            else:
                result += tagList[i] 
        if len(tagList) < len(elseList):
            result += elseList[-1]
        if not self.silent:
            self.fout.write(result)
        return result


def main(argv):
    f = open("word_filter_out.pickle",'r')   
    #filter.pickle is the pickle docs that store the filterList
    fin = open(argv[1],"r")
    fout = open(argv[2],"w")        
    doer = Filter(f, fin, fout)
    doer.filter()    
    fout.close()
    fin.close()
    f.close()


if __name__ == "__main__":
    main(sys.argv)
