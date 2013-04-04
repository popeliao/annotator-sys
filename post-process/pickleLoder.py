# -*- coding: utf-8 -*-
#from countryName.dat load the countryName list
import pickle
import sys

def main(argv):
    load_pickle(argv[1])

def load_pickle(filename):
    f = open(filename,'r')
    print "Loading %s" %(filename)
    pickleList = pickle.load(f)    
    f.close()
    return pickleList

if __name__ == "__main__":
    main(sys.argv)