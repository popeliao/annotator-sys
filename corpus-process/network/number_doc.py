#number_doc
#function: number all the doc, i.e <doc> -> <doc i>

import sys
import re


def main(argv):
    f = open(argv[1],"r")
    fout = open(argv[2],"w")    
    i = 0
    for line in f:
        if '<doc>' in line:
            i += 1
            fout.write('<doc %d>\n' %(i))
        else:
            fout.write(line)
    f.close()
    fout.close()


if __name__ == "__main__":
    main(sys.argv)


                 