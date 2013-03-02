import os
import sys

def EOLdealer(st):
        tmp = st.replace('\r\n','\n')
	fout.write(tmp.replace('\r','\n'))

def main(argv):
	f = open(argv[1],"rb")
	s = f.read()
	f.close()

	fout = open(argv[2],"w")
	s = EOLdealer(s)
	fout.close()


if __name__ == "__main__":
	main(sys.argv)
