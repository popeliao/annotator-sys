fRecord = open("result.txt","w")
f1 = open("150_200_a_a.txt","r")     #t1 is response
f2 = open("150_200_a_p.txt","r")     #t2 is key
#f1 = open("t1.txt","r")     #t1 is response
#f2 = open("t2.txt","r")     #t2 is key

COR = 0
INC = 1
PAR = 2
MIS = 3
SUP = 4

pos1 = [] 
NERtype1 = []
strRecorder1 = []
pos2 = []
NERtype2 = []
strRecorder2 = []

#store stat data for each doc
ansLOC = {}
ansLOC[COR] = {}
ansLOC[INC] = {}

ansNER = {}
ansNER["PERSON"] = {}
ansNER["ORGANIZATION"] = {}

docNum = 0
#store stat data for the whole
sumAnsLOC = {}
sumAnsLOC[COR] = {}
sumAnsLOC[INC] = {}

sumAnsNER = {}
sumAnsNER["PERSON"] = {}
sumAnsNER["ORGANIZATION"] = {}

#init for the summary stat data
sumAnsLOC[COR][COR] = 0
sumAnsLOC[COR][INC] = 0
sumAnsLOC[COR][PAR] = 0
sumAnsLOC[COR][MIS] = 0
sumAnsLOC[COR][SUP] = 0

sumAnsLOC[INC][COR] = 0
sumAnsLOC[INC][INC] = 0
sumAnsLOC[INC][PAR] = 0
sumAnsLOC[INC][MIS] = 0
sumAnsLOC[INC][SUP] = 0    

sumAnsNER["PERSON"][COR] = 0
sumAnsNER["PERSON"][INC] = 0
sumAnsNER["PERSON"][PAR] = 0
sumAnsNER["PERSON"][MIS] = 0
sumAnsNER["PERSON"][SUP] = 0

sumAnsNER["ORGANIZATION"][COR] = 0
sumAnsNER["ORGANIZATION"][INC] = 0
sumAnsNER["ORGANIZATION"][PAR] = 0
sumAnsNER["ORGANIZATION"][MIS] = 0
sumAnsNER["ORGANIZATION"][SUP] = 0

def init():  
    global pos1,pos2,NERtype1,NERtype2,strRecorder1,strRecorder2
    global ansLOC,ansNER
    pos1 = [] 
    NERtype1 = []
    strRecorder1 = []
    pos2 = []
    NERtype2 = []
    strRecorder2 = []

    #first dim = COR or INC to indicate type tagging correctness
    ansLOC[COR][COR] = 0
    ansLOC[COR][INC] = 0
    ansLOC[COR][PAR] = 0
    ansLOC[COR][MIS] = 0
    ansLOC[COR][SUP] = 0

    ansLOC[INC][COR] = 0
    ansLOC[INC][INC] = 0
    ansLOC[INC][PAR] = 0
    ansLOC[INC][MIS] = 0
    ansLOC[INC][SUP] = 0    

    ansNER["PERSON"][COR] = 0
    ansNER["PERSON"][INC] = 0
    ansNER["PERSON"][PAR] = 0
    ansNER["PERSON"][MIS] = 0
    ansNER["PERSON"][SUP] = 0

    ansNER["ORGANIZATION"][COR] = 0
    ansNER["ORGANIZATION"][INC] = 0
    ansNER["ORGANIZATION"][PAR] = 0
    ansNER["ORGANIZATION"][MIS] = 0
    ansNER["ORGANIZATION"][SUP] = 0

    


def printStat():
    fRecord.write("\nStat for LOCATION\n")
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("TYPE/POS","COR","INC","PAR","MIS","SUP"))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("COR",ansLOC[COR][COR],ansLOC[COR][INC],ansLOC[COR][PAR],ansLOC[COR][MIS],ansLOC[COR][SUP]))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("INC",ansLOC[INC][COR],ansLOC[INC][INC],ansLOC[INC][PAR],"N\A","N\A"))
    
    fRecord.write("\nStat for LOCATION tagged as other NE\n")
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("TYPE/POS","COR","INC","PAR","MIS","SUP"))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("PER",ansNER["PERSON"][COR],ansNER["PERSON"][INC],ansNER["PERSON"][PAR],ansNER["PERSON"][MIS],ansNER["PERSON"][SUP]))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("ORG",ansNER["ORGANIZATION"][COR],ansNER["ORGANIZATION"][INC],ansNER["ORGANIZATION"][PAR],ansNER["ORGANIZATION"][MIS],ansNER["ORGANIZATION"][SUP]))

def sumRecord():
#sum up the value to the summary
    sumAnsLOC[COR][COR] = sumAnsLOC[COR][COR] + ansLOC[COR][COR]
    sumAnsLOC[COR][INC] = sumAnsLOC[COR][INC] + ansLOC[COR][INC]
    sumAnsLOC[COR][PAR] = sumAnsLOC[COR][PAR] + ansLOC[COR][PAR]
    sumAnsLOC[COR][MIS] = sumAnsLOC[COR][MIS] + ansLOC[COR][MIS]
    sumAnsLOC[COR][SUP] = sumAnsLOC[COR][SUP] + ansLOC[COR][SUP]

    sumAnsLOC[INC][COR] = sumAnsLOC[INC][COR] + ansLOC[INC][COR]
    sumAnsLOC[INC][INC] = sumAnsLOC[INC][INC] + ansLOC[INC][INC]
    sumAnsLOC[INC][PAR] = sumAnsLOC[INC][PAR] + ansLOC[INC][PAR]
    sumAnsLOC[INC][MIS] = sumAnsLOC[INC][MIS] + ansLOC[INC][MIS]
    sumAnsLOC[INC][SUP] = sumAnsLOC[INC][SUP] + ansLOC[INC][SUP]

    sumAnsNER["PERSON"][COR] = sumAnsNER["PERSON"][COR] + ansNER["PERSON"][COR]
    sumAnsNER["PERSON"][INC] = sumAnsNER["PERSON"][INC] + ansNER["PERSON"][INC]
    sumAnsNER["PERSON"][PAR] = sumAnsNER["PERSON"][PAR] + ansNER["PERSON"][PAR]
    sumAnsNER["PERSON"][MIS] = sumAnsNER["PERSON"][MIS] + ansNER["PERSON"][MIS]
    sumAnsNER["PERSON"][SUP] = sumAnsNER["PERSON"][SUP] + ansNER["PERSON"][SUP]

    sumAnsNER["ORGANIZATION"][COR] = sumAnsNER["ORGANIZATION"][COR] + ansNER["ORGANIZATION"][COR]
    sumAnsNER["ORGANIZATION"][INC] = sumAnsNER["ORGANIZATION"][INC] + ansNER["ORGANIZATION"][INC]
    sumAnsNER["ORGANIZATION"][PAR] = sumAnsNER["ORGANIZATION"][PAR] + ansNER["ORGANIZATION"][PAR]
    sumAnsNER["ORGANIZATION"][MIS] = sumAnsNER["ORGANIZATION"][MIS] + ansNER["ORGANIZATION"][MIS]
    sumAnsNER["ORGANIZATION"][SUP] = sumAnsNER["ORGANIZATION"][SUP] + ansNER["ORGANIZATION"][SUP]

def record(ACT, p, q):
    #record each item and make the stat data for each doc
    if (ACT <> MIS and ACT <> SUP):
        if ( NERtype1[p] == NERtype2[q]): #****
            typeFlag = "COR"
        else:
            typeFlag = "INC"
    else:
        if (ACT == MIS):
            typeFlag = "MIS"
        if (ACT == SUP):
            typeFlag = "SUP"
    if (ACT == COR):        
        fRecord.write("%10s%5s%50s%50s" %("COR", typeFlag, strRecorder1[p], strRecorder2[q]))
    elif (ACT == INC):
        fRecord.write("%10s%5s%50s%50s" %("INC", typeFlag, strRecorder1[p], strRecorder2[q]))
    elif (ACT == PAR):
        fRecord.write("%10s%5s%50s%50s" %("PAR", typeFlag, strRecorder1[p], strRecorder2[q]))
    elif (ACT == MIS):
        fRecord.write("%10s%5s%50s%50s" %("MIS", typeFlag, "", strRecorder2[q]))
    elif (ACT == SUP):
        fRecord.write("%10s%5s%50s%50s" %("SUP", typeFlag, strRecorder1[p], ""))
    
    fRecord.write("\n")

    #make stat for LOC
    if (ACT <> MIS and ACT <> SUP):
        if (NERtype2[q]=="LOCATION" and NERtype1[p] == NERtype2[q]): #******
            ansLOC[COR][ACT] = ansLOC[COR][ACT] + 1
        elif (NERtype2[q]=="LOCATION" and NERtype1[p] <> NERtype2[q]): #*****
            ansLOC[INC][ACT] = ansLOC[INC][ACT] + 1
    else:
        if (ACT == MIS):
            if (NERtype2[q]=="LOCATION"):
                ansLOC[COR][MIS] = ansLOC[COR][MIS] + 1                        
        if (ACT == SUP):
            if (NERtype1[p]=="LOCATION"):
                ansLOC[COR][SUP] = ansLOC[COR][SUP] + 1            

    #make stat for all NE, i.e. those LOC tagged as other NE
    if (ACT <> MIS and ACT <> SUP):
        if (p < len (NERtype1) and q < len (NERtype2) and NERtype2[q]=="LOCATION" and NERtype1[p]<>"LOCATION"): #*****
            ansNER[NERtype1[p]][ACT] = ansNER[NERtype1[p]][ACT] + 1            

def compare():
    p = 0
    q = 0
    #print pos1
    #print pos2
    #print len(pos1),len(pos2),"****"
    while (p < len(pos1) and q < len(pos2)) :
        if (pos1[p][1] < pos2[q][0]):
            #if (NERtype1[p] == "LOCATION"):
            record(SUP, p, q)
            p = p + 1
        elif(pos1[p][1] < pos2[q][1]):
            if (pos1[p][0] < pos2[q][0]):
                record(INC, p, q)
            else:
                record(PAR, p, q)
            p = p + 1
        elif(pos1[p][1] == pos2[q][1]):
            if (pos1[p][0] < pos2[q][0]):
                record(INC, p, q)
            elif (pos1[p][0] == pos2[q][0]):
                record(COR, p, q)
            else:
                record(PAR, p, q)
            p = p + 1
            q = q + 1
        else:
            if (pos1[p][0] <= pos2[q][1]):
                record(INC, p, q)
            else:
                record(MIS, p, q)
            q = q + 1
    if (p < len(pos1)):
        #if (NERtype1[p] == "LOCATION"):
        record(SUP, p, q)
        p = p + 1
    if (q < len(pos2)):
        record(MIS, p, q)
        q = q + 1


def extractDoc(s, pos, NERtype, strRecorder):
    #print s
    NER_tmp = ""  #tmp var to store char inside parentheses
    str_tmp = ""  #tmp var to store char of a tagged content
    i = 0         #number of char
    pn = 0        #number of parentheses
    
    sp = 0        #pointer of string s
    c = s[sp]     #store current char
    sp = sp + 1
    sn = len(s)
    inside = False   #the state to indicate inside a parent or not
    openFlag = True  #the state to indicate current parent is an open one
    while (sp < sn):            
        global docNum
        #if (docNum == 1):
	    #    print c,i    
        if (c == '<'):        
            if (openFlag):
                pos.append([])
                pos[pn].append(i)
                openFlag = False            
            else:
                pos[pn].append(i - 1)
                strRecorder.append(str_tmp)
                str_tmp = ""
                openFlag = True
                pn = pn + 1
            i = i - 1
            inside = True
        if (c == '>'):        
            inside = False
            if (not openFlag):
                NERtype.append(NER_tmp)
                NER_tmp = ""    
        c = s[sp]
        sp = sp + 1
        if (not inside):
            i = i + 1
            if (not openFlag and c <> '<'):
                str_tmp = str_tmp + c
        else:
            if (not openFlag and c <> '>'):
                NER_tmp = NER_tmp + c
    #
    #global docNum
    #if (docNum == 1 or docNum == 2):
    #print pos, NERtype, strRecorder

def printSum():
    
    fRecord.write("\n\n\n***************************\nStat for all doc\n**************************\n")
    fRecord.write("\nStat for LOCATION\n")
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("TYPE/POS","COR","INC","PAR","MIS","SUP"))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("COR",sumAnsLOC[COR][COR],sumAnsLOC[COR][INC],sumAnsLOC[COR][PAR],sumAnsLOC[COR][MIS],sumAnsLOC[COR][SUP]))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("INC",sumAnsLOC[INC][COR],sumAnsLOC[INC][INC],sumAnsLOC[INC][PAR],"N\A","N\A"))
    
    fRecord.write("\nStat for LOCATION tagged as other NE\n")
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("TYPE/POS","COR","INC","PAR","MIS","SUP"))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("PER",sumAnsNER["PERSON"][COR],sumAnsNER["PERSON"][INC],sumAnsNER["PERSON"][PAR],sumAnsNER["PERSON"][MIS],sumAnsNER["PERSON"][SUP]))
    fRecord.write("%10s%5s%5s%5s%5s%5s\n" %("ORG",sumAnsNER["ORGANIZATION"][COR],sumAnsNER["ORGANIZATION"][INC],sumAnsNER["ORGANIZATION"][PAR],sumAnsNER["ORGANIZATION"][MIS],sumAnsNER["ORGANIZATION"][SUP]))

def dealDocly():
    c1 = f1.readline()
    c2 = f2.readline()
    while c1:
        while not "<doc>" in c1:
            c1 = f1.readline()
        while not "<doc>" in c2:
            c2 = f2.readline()
        s1 = ""
        s2 = ""
        c1 = f1.readline()
        c2 = f2.readline()
        while not "</doc>" in c1:
            s1 = s1 + c1
            c1 = f1.readline()
        while not "</doc>" in c2:
            s2 = s2 + c2
            c2 = f2.readline()

        global docNum
        docNum = docNum + 1
        #print docNum
        fRecord.write("---------------------------------------------------------------------------------------------------------------------\n")
        fRecord.write("Summary for Doc" + str(docNum) + "\n")
        fRecord.write("%10s%5s%50s%50s\n" %("POSITION","TYPE","RSP_TEXT","KEY_TEXT"))
        init()
        extractDoc(s1, pos1, NERtype1, strRecorder1) #t1 is response
        extractDoc(s2, pos2, NERtype2, strRecorder2) #t2 is key
        compare()
        printStat()       
        sumRecord()    

        c1 = f1.readline()
        c2 = f2.readline()   
        
#############main##################

dealDocly()
printSum()

f1.close()
f2.close()
fRecord.close()

#print ansNER
#print ansLOC
