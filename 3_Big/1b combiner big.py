import os

allfiles = os.listdir(os.getcwd())
listoffiles = []

for item in allfiles: # go through all files and find the relevant ones
    helper = item.split('.')
    if len(helper) == 3: # it is the right filetype
        listoffiles.append(helper[1])

print 'The directory has been scanned and these are the relevant files found:'

for i in listoffiles:
    print i

right = raw_input("Please enter the file you want to scan.\n")

while right not in listoffiles:
    print 'It was not possible to read your input. \nPlease chose one of the files available!\n'
    for i in listoffiles:
        print i
    right = raw_input("Please enter the number of the file you want to scan.\n")

filename = 'medium.' + str(right) + '.txt'
outputname = 'Layer Big ' + str(right) + '.dat'
f = open(outputname,'w+')
g = open(filename,'r')
h = open('all the rest.txt','r')

st = 1
nd = 0
rd = 0
sthalf = 1
ndhalf = 0

for line in h: # write first part of all the rest
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'FIRST' and text[1] == 'STOP':
            st = 0
    if st == 1 and len(text) > 0 and text[0] != 'FIRST':
        f.write(line)

h.close()

for line in g: # write first part of output
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'MIDDLE' and text[1] == 'REACHED':
            sthalf = 0
    if sthalf == 1 and len(text) > 0 and text[0] != 'MIDDLE': # middle is written in writer only for PERMK
        f.write(line)

g.close()
h = open('all the rest.txt','r')

for line in h: # write second part of all the rest
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'FIRST' and text[1] == 'STOP':
            nd = 1
        if text[0] == 'SECOND' and text[1] == 'STOP':
            nd = 0
    if nd == 1 and  len(text) > 0 and text[0] != 'FIRST' and text[0] != 'SECOND':
        f.write(line)

h.close()
g = open(filename,'r')

for line in g: # write second part of output
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'MIDDLE' and text[1] == 'REACHED':
            ndhalf = 1
    if ndhalf == 1 and len(text) > 0 and text[0] != 'MIDDLE':
        f.write(line)

g.close()
h = open('all the rest.txt','r')

for line in h: # write third part of all the rest
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'SECOND' and text[1] == 'STOP':
            rd = 1
    if rd == 1 and len(text) > 0 and text[0] != 'SECOND':
        f.write(line)

f.close()
h.close()
