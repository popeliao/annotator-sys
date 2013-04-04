# -*- coding: utf-8 -*-
#function:  extract filter keywords from argv[1](*.dat) into a list
#           write the dict into argv[2](*.pickle) using pickle

import sys
import re
import pickle

def main(argv):
    f = open(argv[1],"r")
    fout = open(argv[2],"w")    
    i = 0
    countryList = []
    for line in f:
        countryList.append(line[:-1])
    pickle.dump(countryList, fout)
    f.close()
    fout.close()


if __name__ == "__main__":
    main(sys.argv)
