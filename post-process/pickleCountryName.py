#from countryName.dat load the countryName list
import pickle
f = open("countryName.dat",'r')
countryNameList = pickle.load(f)
print countryNameList
f.close()