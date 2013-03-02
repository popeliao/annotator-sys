#deleteHttp
#function 1: delete all the '<' and '>' in <http:...> like content,
#This can be done both for tagged file and untagged file

import sys
import re


def main(argv):
	f = open(argv[1],"r")
	fout = open(argv[2],"w")
	p = re.compile(r'<(http.*?)>')
	#delete all matched http annotation
	#and write them in the fout file
	s = f.read()
	fout.write( p.sub(r'\1', s))
	f.close()
	fout.close()


if __name__ == "__main__":
	main(sys.argv)
