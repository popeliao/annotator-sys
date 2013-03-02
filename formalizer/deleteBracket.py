#pre-formalizer
#function 1: delete all the '<' and '>' from raw dataset
#And it must save all the the '<' and '>' that appear in <doc> </doc> like position 

import sys
import string


def main(argv):
    f = open(argv[1], "r")
    s = f.read()
    s = s.replace('<doc>','?doc?').replace('</doc>','?/doc?')
    s = s.translate(string.maketrans('',''),'<>')
    s = s.replace('?doc?','<doc>').replace('?/doc?','</doc>')
    f.close()
    f = open(argv[2], "w")
    f.write(s)     
    f.close()
    



if __name__ == "__main__":
	main(sys.argv)
