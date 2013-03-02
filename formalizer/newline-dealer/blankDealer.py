#blankDealer
#function: trimming all leading and trailing blank char

import sys
import re


def blankTrim(st):
	p = re.compile(r'\n( +)')		
	tmp = p.sub(r'\n', st)
	p = re.compile(r'( +)\n')
	return p.sub(r'\n', tmp)

def main(argv):
	f = open(argv[1],"r")
	fout = open(argv[2],"w")
	
	s = f.read()
	s = blankTrim(s)
	
	fout.write(s)
	f.close()
	fout.close()


if __name__ == "__main__":
	main(sys.argv)

