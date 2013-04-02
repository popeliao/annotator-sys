# -*- coding: utf-8 -*-
#extractCountry
#function:  extract Country name from argv[1] into a list
#           write the dict into argv[2] using pickle

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
