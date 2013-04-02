# -*- coding: utf-8 -*-
#from countryName.dat load the countryName list
import pickle
f = open("countryName.pickle",'r')
countryNameList = pickle.load(f)
print countryNameList
f.close()