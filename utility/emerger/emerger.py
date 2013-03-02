#functionality interface
#input: file 1 unannotated docs without < > other than <doc>
#       file 2 annotated docs maybe with extra < >
#		file 3 the merged doc to be written in 
#output:write the annoated docs
#       without extra < > that appears in file 3
#		if some differences occurs between file 1 and file 2, print that on the screen
import sys

col = [None]*2
line = [None]*2
c = [None]*2
p = [None]*2
s = [None]*2
output = ""


def moveOn(i):
    global f0,f1,f2,s,col,line,c,p,output
    col[i] += 1
    p[i] += 1
    c[i] = s[i][p[i]]
    if (c[i] == '\n'):
        line[i] += 1
        col[i] = 1
        
def init():
    global f0,f1,f2,s,col,line,c,p,output
    s[0] = f0.read()
    p[0] = 0    
    line[0] = 1
    col[0] = 1
    s[1] = f1.read()
    p[1] = 0    
    line[1] = 1
    col[1] = 1    

def printErr():
    global f0,f1,f2,s,col,line,c,p,output
    print "Diff occurs"
    print "file 1: line %d col %d" %(line[0], col[0])
    print "file 2: line %d col %d" %(line[1], col[1])
    print "char in file1 is: "+str(c[0])
    print "char in file2 is: "+str(c[1])

def isNested(p,ss):
    i = p
    while i < len(ss) and ss[i] <> '>':
        i += 1
        if ss[i] == '<':
            return True, -1
    return False, i

def isLegalNER(begin,end,ss):
    global f0,f1,f2,s,col,line,c,p,output
    stmp = ss[begin+1:end]
    if (stmp[0:3] in ['/NE','NE:']):
        output += ss[begin:end+1]
        return True
    else:
        return False

def merge():
    global f0,f1,f2,s,col,line,c,p,output
    init()
    s0n = len(s[0])
    s1n = len(s[1])
    s[0] += '$'
    s[1] += '$'   #make a end safer to avoid out of range error
    while p[0]<s0n and p[1]<s1n:
        c[0] = s[0][p[0]]
        c[1] = s[1][p[1]]        
        #move on based on judgment
        if (c[0] <> c[1]):
            if (c[1] == '<'):
                nested, end = isNested(p[1],s[1])
                if nested:
                    moveOn(1)
                else:
                    if isLegalNER(p[1],end,s[1]):
                    #the char needed to output has printed if legal
                        while (p[1] <> end + 1):
                            moveOn(1)                                                
                    else:
                        return printErr()
            elif (c[1] == '>'):
                moveOn(1)
            else: # c1 is neither '<' nor '>'
                return printErr()
        else:
            output += c[0]
            moveOn(0)
            moveOn(1)
    if p[0]<s0n:
        print "file 1 has extra thing at the end of the file"
    elif p[1]<s1n:
        print "file 2 has extra thing at the end of the file"
    else:
        print "Emerge successfully! :)"

def main(argv):
    global f0,f1,f2,s,col,line,c,p,output
    f0 = open(argv[1], "r")
    f1 = open(argv[2], "r")
    merge()             
    f0.close()
    f1.close()
    f2 = open(argv[3],"w")
    f2.write(output)
    f2.close()

if __name__ == "__main__":
    main(sys.argv)
