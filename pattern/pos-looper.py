filename = "test.txt"
f = open(filename, "r")
s = f.read()
p = 0
sn = len(s)
line = 1
col = 1
while p<sn:
    c = s[p]
    #deal with c
    col = col + 1
    if (c == '\n'):
        line = line + 1
        col = 1
    p = p + 1
f.close()
