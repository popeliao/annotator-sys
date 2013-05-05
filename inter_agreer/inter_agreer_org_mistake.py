# A COPY OF inter_agree.py FOR KEEP TRACK OF MIS MISTAKE OF CITY
# IN ORDER TO SEE WHETHER MOST OF THEM IS INSIDE A ORGANIZATION RECOGNINION

#main->type_iter 
#     dealDocly                                ->compare                   ->printAllStat
#    :extractDoc(pos, NERtype, strRecorder)    :record
#                                              :recordStat (tp,fp,tn,fn)
#
# The adaption for each iteration one type made is in extractDoc

fRecord = open("result.txt","w")

#classes
annotate_type = [["NE:CIT","/NE:CI"],["NE:ORG","/NE:OR"],["NE:LOC","/NE:LO"]]
g_i = 0
annotate_type_name = ["CITY","ORGANIZATION","LOCATION"]

#For keep track of all organization position in response.txt
g_mis = 0
g_mis_orz = 0
org_pos_1 = []

def type_iter():    
    #iterate the whole docs but only judge one tyep
    global g_i,docNum
    global pos1
    for g_i in range(3):
        docNum = 0
        f1 = open("response.txt","r")     #t1 is response
        f2 = open("key.txt","r")     #t2 is key
        
        fRecord.write("\n\n\n***************************\nagreement result for %s\n**************************\n" %(annotate_type_name[g_i]))
        dealDocly(f1, f2)
        printAllStat()
        if g_i == 0:
            fRecord.write("For CITY annotation\n")
            fRecord.write("All missing: %d   The missing mistake that is marked as organization: %d" %(g_mis, g_mis_orz))
        f1.close()
        f2.close()
       
    


def printAllStat():
    #print all measure stat data based tp,tn,fp,fn
    global tp,tn,fp,fn, g_i
    pr = tp/float(tp+fp)
    re = tp/float(tp+fn)
    F = 2*pr*re/float(pr+re)
    fRecord.write("\n\n\n***************************\nStat for all doc regarding type: %s\n**************************\n" %(annotate_type_name[g_i]))
    fRecord.write("%10s %5f\n" %("precision:",pr))
    fRecord.write("%10s %5f\n" %("recall:",re))
    fRecord.write("%10s %5f\n" %("F-measure:",F))


#stat info
#true postive, false postive, true negative, false negative
tp=0
fp=0
tn=0
fn=0


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

def recordStat(ACT, typeFlag):
    #dynamically change the global value tp,tn,fp,fn based on record 
    #ACT(postion) and typeFlag(type), see about_measure for reference
    global tp,tn,fp,fn
    #strictly matching for postion, don't care type  
    if ACT == MIS:
        fn += 1
        if g_i == 0:
            global g_mis
            g_mis += 1
    elif ACT == COR:
        tp += 1
    else:
        fp += 1

 
def record(ACT, p, q):
    #This part gathers missing mistake that is actually annoated by NE:ORG
    if g_i == 0: # it is record for CITY annotation
        global g_mis_orz, org_pos_1
        if ACT == MIS:
            for [begin, end] in org_pos_1:
                if (pos2[q][0] > end or pos2[q][1] < begin):
                    pass
                else:
                    g_mis_orz += 1
                    break
    #record each item and make the stat data for each doc
    if (ACT <> MIS and ACT <> SUP):
        if ( NERtype1[p] == NERtype2[q]): 
            typeFlag = "COR"
        else:
            typeFlag = "INC"
    else:
        if (ACT == MIS):
            typeFlag = "MIS"
        if (ACT == SUP):
            typeFlag = "SUP"
    if (ACT == COR):        
        fRecord.write("%s\nRSP==  %s\nKEY==  %s\n" %("COR", strRecorder1[p], strRecorder2[q]))
    elif (ACT == INC):
        fRecord.write("%s\nRSP==  %s\nKEY==  %s\n" %("INC", strRecorder1[p], strRecorder2[q]))        
    elif (ACT == PAR):
        fRecord.write("%s\nRSP==  %s\nKEY==  %s\n" %("PAR", strRecorder1[p], strRecorder2[q]))        
    elif (ACT == MIS):
        fRecord.write("%s\nRSP==  %s\nKEY==  %s\n" %("MIS", "", strRecorder2[q]))        
    elif (ACT == SUP):
        fRecord.write("%s\nRSP==  %s\nKEY==  %s\n" %("SUP", strRecorder1[p], ""))        
    fRecord.write("-----------------\n")
    recordStat(ACT, typeFlag)
   
def compare():
    p = 0
    q = 0
    while (p < len(pos1) and q < len(pos2)) :
        if (pos1[p][1] < pos2[q][0]):
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
    while (p < len(pos1)):
        record(SUP, p, q)
        p = p + 1
    while (q < len(pos2)):
        record(MIS, p, q)
        q = q + 1

def extractDoc_with_context(s, pos, NERtype, strRecorder):
    global g_i    #we're dealing with g_i th ner type
    NER_tmp = ""  #tmp var to store char inside parentheses
    str_tmp = ""  #tmp var to store char of a tagged content
    i = 0         #number of char
    sp = 0        #pointer of string s
    c = s[sp]     #store current char
    sp = sp + 1
    sn = len(s)
    inside = False   #the state to indicate inside a parent or not
    openFlag = False  #the state to indicate last parent is an open one
    while (sp < sn):
        if c=='<':
            inside = True            
        if (not inside):
            i = i + 1
            if (openFlag and c <> '<' and c <> '<'):
                str_tmp = str_tmp + c
        else:
            if (c <> '>' and c <> '<'):
                NER_tmp = NER_tmp + c    
        if c=='>':
            inside = False
            if (NER_tmp[:6] in annotate_type[g_i]):
                openFlag = not openFlag
                if openFlag:
                    start = i
                    start_abs = sp - 30 if sp - 30 > 0 else 0
                    NER_tmp = ""
                else:
                    end = i
                    pos.append([start,end])
                    NERtype.append(NER_tmp)
                    str_tmp = s[start_abs:sp + 30].replace('\n',' ') # make it included context
                    strRecorder.append(str_tmp)
                    str_tmp = NER_tmp = ""
            else:
                NER_tmp = ""
        c = s[sp]
        sp = sp + 1                       

def extractDoc(s, pos, NERtype, strRecorder):
    global g_i	  #we're dealing with g_i th ner type
    NER_tmp = ""  #tmp var to store char inside parentheses
    str_tmp = ""  #tmp var to store char of a tagged content
    i = 0         #number of char
    sp = 0        #pointer of string s
    c = s[sp]     #store current char
    sp = sp + 1
    sn = len(s)
    inside = False   #the state to indicate inside a parent or not
    openFlag = False  #the state to indicate last parent is an open one
    while (sp < sn):
        if c=='<':
            inside = True            
        if (not inside):
            i = i + 1
            if (openFlag and c <> '<' and c <> '<'):
                str_tmp = str_tmp + c
        else:
            if (c <> '>' and c <> '<'):
                NER_tmp = NER_tmp + c    
        if c=='>':
            inside = False
            if (NER_tmp[:6] in annotate_type[g_i]):
                openFlag = not openFlag
                if openFlag:
                    start = i
                    NER_tmp = ""
                else:
                    end = i
                    pos.append([start,end])
                    NERtype.append(NER_tmp)
                    strRecorder.append(str_tmp)
                    str_tmp = NER_tmp = ""
            else:
                NER_tmp = ""
        c = s[sp]
        sp = sp + 1                       


def dealDocly(f1,f2):
    c1 = f1.readline()
    c2 = f2.readline()
    while c1:
        while c1 and not "<doc>" in c1:
            c1 = f1.readline()
        while c2 and not "<doc>" in c2:
            c2 = f2.readline()
        if c1 and c2:
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
            fRecord.write("-----------------\n")            
            init()

            global g_i, org_pos_1
            if g_i == 0: # it is a CITY annotation
                g_i = 1 # change mode to ORG
                extractDoc_with_context(s1, pos1, NERtype1, strRecorder1) #t1 is response
                org_pos_1 = pos1[:]
                init()
                g_i = 0
                extractDoc_with_context(s1, pos1, NERtype1, strRecorder1) #t1 is response
                extractDoc_with_context(s2, pos2, NERtype2, strRecorder2) #t2 is key                
            else:
                extractDoc_with_context(s1, pos1, NERtype1, strRecorder1) #t1 is response
                extractDoc_with_context(s2, pos2, NERtype2, strRecorder2) #t2 is key

"""DEBUG            print pos1
            print strRecorder1
            print '**************'
            print pos2 
            print strRecorder2
            print '**************'"""
            compare()   #in compare func, we does 3 things
                        #1 we record all the details 
                        #2 we print all the details
                        #3 we make stat data based on the details        
            c1 = f1.readline()
            c2 = f2.readline()   
        
#############main##################

type_iter()
fRecord.close()
