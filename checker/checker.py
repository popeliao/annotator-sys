#program to check consistency of annoated data
#by Ruizhi Feb,2013
import sys
    

SingleLEFT = 0
SingleRIGHT = 1
Blanced = 2

def checkBlance(f):
    c = f.read(1)
    balance = 0
    linePos = 1
    pos = 1

    while c:
        #print c + str(linePos) + "," + str(pos) + ":" + str(balance)
        if (c == '<'):
            balance = balance + 1
        if (c == '>'):
            balance = balance - 1
        if (c == '\n'):
            linePos = linePos + 1
            pos = 1
        if (balance == 2):
            return (SingleLEFT, l, p)
        if (balance == -1):
            return (SingleRIGHT, linePos, pos)
        if (c == '<'):
            l = linePos
            p = pos
        pos = pos + 1  
        c = f.read(1)
    return (Blanced,0,0)


UnMatched = 1
SingleOpen = 2
SingleClosed = 3
Matched = 4

dictNER = {}
def checkConsistency(f):
    NER_tmp = ""  #tmp var to store char inside parentheses
    i = 0         #number of char
    
    c = f.read(1)     #store current char
    inside = False   #the state to indicate inside a parent or not
    
    linePos = 1
    pos = 1
    aStack = []
    posS = []
    while (c):
        if (inside):
            NER_tmp = NER_tmp + c
        if (c == '\n'):
            linePos = linePos + 1
            pos = 1
        if (c == '<'):
            inside = True
            NER_tmp = ""
        if (c == '>'):  
            inside = False
            if (NER_tmp[0:4] <> "http"): #not a url
      #          dictNER[NER_tmp] = 1
                if (NER_tmp[0] == '/'):
                    if (not aStack):          #case 1: nothing to match
                        return (SingleClosed, linePos, pos)
                    elif (aStack[len(aStack)-1][:5] == NER_tmp[1:6]):         #case 2: matched successfully
                        aStack.pop()
                        posS.pop()
                    else:                #case 3: cannot match
                        return (UnMatched, linePos, pos, posS[len(posS)-1][0], posS[len(posS)-1][1])
                else: #push into stack a open tag
                    aStack.append(NER_tmp) 
                    posS.append([linePos, pos])
        c = f.read(1)
        pos = pos + 1

    if (aStack): #some open tag doesn't have close tag matched
        return (SingleOpen, posS[len(aStack)-1][0], posS[len(aStack)-1][1])
    else:
        return (Matched, 0, 0)

def main(argv):
    filename = argv[1]
    f = open(filename,"r")  
    rel = checkBlance(f)
    f.close()
    if (rel[0] == Blanced):
        f = open(filename,"r")   
        rel2 = checkConsistency(f)
        f.close()        
        if (rel2[0] == Matched):
            print "Check passed!"
        elif (rel2[0] == UnMatched):
            print "Unmatched annotation at line " + str(rel2[3]) + ',' + str(rel2[4]) + " and at line " + str(rel2[1]) + ',' + str(rel2[2]) 
        elif (rel2[0] == SingleOpen):
            print "Single open annotation at line " + str(rel2[1]) + ',' + str(rel2[2])
        elif (rel2[0] == SingleClosed):
            print "Single closed annotation at line " + str(rel2[1]) + ',' + str(rel2[2])

    elif (rel[0] == SingleLEFT):
        print "Single Left bracket at line " + str(rel[1]) + ',' + str(rel[2])
    elif (rel[0] == SingleRIGHT):
        print "Single Right bracket at line " + str(rel[1]) + ',' + str(rel[2])

   #print dictNER


#############main##################
if __name__ == "__main__":
	main(sys.argv)
