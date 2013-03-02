#Bracket-stat
#A tool to produce stat data for a doc

import string
import re
beforeLeft = {}
afterLeft = {}
beforeRight = {}
afterRight = {}

filename = "psb_first_50_of_200.txt"

f = open(filename,"r")
p1 = re.compile(r'(.{,3})(<)(.{,3})')
for line in f:
    m = p1.search(line)
    while m:
        beforeLeft[m.group(1)] = 1
        afterLeft[m.group(3)] = 1
        m = p1.search(line, m.start(2) + 1)
f.close()

f = open(filename,"r")
p2 = re.compile(r'(.{,3})(>)(.{,3})')
for line in f:
    m = p2.search(line)
    while m:
        beforeRight[m.group(1)] = 1
        afterRight[m.group(3)] = 1
        m = p2.search(line, m.start(2) + 1)
f.close()


print 'left bracket stat:'
print "-------------left---before-------------------------"
print beforeLeft.keys()
print "-------------left---after-------------------------"
print afterLeft.keys()
print 'right bracket stat:'
print "-------------right--before-------------------------"
print beforeRight.keys()
print "-------------right--after--------------------------"
print afterRight.keys()
