#recognize full name
#function: get rid of all the person name that contains only one word

import sys
import re


def main(argv):
    f = open(argv[1],"r")
    fout = open(argv[2],"w")
    p = re.compile(r'<NE:IND>([^ ]*?)</NE:IND>')
    s = f.read()
    s = p.sub(r'\1', s)
    fout.write(s)
    f.close()
    fout.close()

if __name__ == "__main__":
    main(sys.argv)
