import blankDealer
import EOLdealer
import 

import sys



def formalize(argv):
    f = open(argv[1],"r")
    fout = open(argv[2],"w")
    p = re.compile(r'\n( +)')	
    s = f.read()
    s = p.sub(r'\n', s)

    p = re.compile(r'( +)\n')
    s = p.sub(r'\n', s)
    fout.write(s)
    
    f.close()
    fout.close()


if __name__ == "__main__":
    formalize(sys.argv)
