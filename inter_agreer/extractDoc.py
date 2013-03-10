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
                else:
                    end = i
                    pos.append([start,end])
                    NERtype.append(NER_tmp)
                    strRecorder.append(str_tmp)
        c = s[sp]
        sp = sp + 1             
                
