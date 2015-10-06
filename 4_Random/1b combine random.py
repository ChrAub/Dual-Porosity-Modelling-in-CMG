import os

allfiles = os.listdir(os.getcwd())
listoffiles = []

for item in allfiles: # go through all files and find the relevant ones
    if item.split('.')[0].split()[0] == 'output':
        print item
        listoffiles.append(item.split('.')[0].split()[1])

if len(listoffiles) == 1:
    selection = listoffiles[0]
else:
    print 'There is more than one file available. Here are the possibilities:'
    for i in listoffiles:
        print i
    selection = raw_input("Please choose the percentage you want to combine!\n")
    while selection not in listoffiles:
        selection = raw_input("Please choose the percentage you want to combine!\n")

inname = 'output ' + selection + '.txt'
outname = 'random ' + selection + '.dat'

f = open(outname,'w+')
g = open(inname,'r')
h = open('2 all the rest random.txt','r')

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
    if sthalf == 1 and len(text) > 0 and text[0] != 'MIDDLE':
        f.write(line)

g.close()
h = open('2 all the rest random.txt','r')

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
g = open(inname,'r')

for line in g: # write second part of output
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'MIDDLE' and text[1] == 'REACHED':
            ndhalf = 1
    if ndhalf == 1 and len(text) > 0 and text[0] != 'MIDDLE':
        f.write(line)

g.close()
h = open('2 all the rest random.txt','r')

for line in h: # write third part of all the rest
    text = line.split()
    print rd
    if len(text) > 0: # ignore empty lines
        if text[0] == 'SECOND' and text[1] == 'STOP':
            rd = 1
    if rd == 1 and len(text) > 0 and text[0] != 'SECOND':
        f.write(line)

f.close()
g.close()
h.close()
