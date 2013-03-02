#reduce all the empty lines
import os
import sys
import re


def main(argv):
	f = open(argv[1],"rb")
	s = f.read()
	f.close()

	p = re.compile(r'\n\n+')
	s = p.sub('\n',s)
	
	fout = open(argv[2],"w")
	s = EOLdealer(s)
	fout.close()


if __name__ == "__main__":
	main(sys.argv)