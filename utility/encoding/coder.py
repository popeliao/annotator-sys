#encoding formalizer
#To be develop

f = open("s.txt","r")
c = f.read(1)
while c:
    print ord(c)
    c = f.read(1)
    
f.close()
