#Tool2city
#function: transform the result produced by NER tool
#to City annotations.

import sys
import re


def main(argv):
	f = open(argv[1],"r")
	fout = open(argv[2],"w")
	p = re.compile(r'(</?PERSON>)')	
	s = f.read()
	s = p.sub(r'', s)

	p = re.compile(r'(</?)ORGANIZATION>')	
	s = p.sub(r'\1NE:ORG>', s)

	p = re.compile(r'(</?)LOCATION>')
	fout.write( p.sub(r'\1NE:CITY>', s))	

	f.close()
	fout.close()


if __name__ == "__main__":
	main(sys.argv)
