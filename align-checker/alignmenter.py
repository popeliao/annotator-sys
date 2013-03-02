#Usage: python alignmenter.py filename1 filename2 

#functionality interface
#input: file 1 unannotated docs 
#       file 2 annotated docs 
#output:print out the result that whether file 1 and file 2 are alignable
#       if not, print out the position where it is different
#assumption: All '<.*?>' is legal NER annotation or <doc>
import sys

class Aligner(object):
    def __init__(self,files):
        self.f0 = files[0]
        self.f1 = files[1]
        self.col = [None]*2
        self.line = [None]*2
        self.c = [None]*2
        self.p = [None]*2
        self.output = ""
        self.s = [None]*2
    def out(self):
        print self.output
        
    def init(self):
        self.s[0] = self.f0.read()
        self.p[0] = -1    
        self.line[0] = 1
        self.col[0] = 0
        self.s[1] = self.f1.read()
        self.p[1] = -1    
        self.line[1] = 1
        self.col[1] = 0    

    def printErr(self):        
        self.output += "file 1: line %d col %d\n" %(self.line[0], self.col[0])
        self.output += "file 2: line %d col %d\n" %(self.line[1], self.col[1])
        self.output += "file1:\t"+str(self.c[0])+"\n"
        self.output += "file2:\t"+str(self.c[1])+"\n"

    def moveOn(self,i):        
        self.col[i] += 1
        self.p[i] += 1
        self.c[i] = self.s[i][self.p[i]]
        if (self.c[i] == '\n'):
            self.line[i] += 1
            self.col[i] = 1
            
    def nextContect(self,i):
        self.moveOn(i)
        changed = True
        while (self.c[i] == '<' and changed):
        #while instead of if because there might be nested annotations
            changed = False
            if (not self.s[i][self.p[i]+1:self.p[i]+4] in ['doc','/do']):
                changed = True
                while (self.c[i] <> '>' ):
                    self.moveOn(i)                    
                self.moveOn(i)
        return self.s[i][self.p[i]]

    def align(self):
        self.init()
        s0n = len(self.s[0])
        s1n = len(self.s[1])
        self.s[0] += '$'
        self.s[1] += '$' #make an end safer to avoid out of range error
        while self.p[0]<s0n and self.p[1]<s1n:
            self.nextContect(0)
            self.nextContect(1)            
            if (self.c[0] <> self.c[1]):
                return self.printErr()
                
        if (self.p[0]<s0n or self.p[1]<s1n):
            return self.printErr()            
        self.output += "Alignment check pass! :)"
                
          
def main(argv):   
    f0 = open(argv[1], "r")
    f1 = open(argv[2], "r")
    doer = Aligner([f0,f1])
    doer.align()
    doer.out()
    f0.close()
    f1.close()

if __name__ == "__main__":
    main(sys.argv)
