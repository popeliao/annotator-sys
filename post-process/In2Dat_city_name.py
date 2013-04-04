# -*- coding: utf-8 -*-
#function:  extract filter keywords from argv[1](*.in) 
#           write keyword into argv[2](*.pickle) each word each line

import sys
import re
import pickle

"""
Sameple format
0        9         0         0         0      7
+  AU APT Alphington                          Alphington                          VIC -----6-- RL 1201      3746S 14501E                                                   
   AU AYD Alroy Downs                         Alroy Downs                         NT  ---4---- AI 9912                                                                     
"""

def main(argv):
    f = open(argv[1],"r")
    fout = open(argv[2],"w")    
    i = 0
    countryList = []
    for line in f:
        keyword = line[10:46].strip()
        fout.write(keyword+'\n')    
    f.close()
    fout.close()


if __name__ == "__main__":
    main(sys.argv)
