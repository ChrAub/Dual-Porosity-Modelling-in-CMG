import os

# read all files in directory and choose the ones that have the relevant ending

allfiles = os.listdir(os.getcwd())
relevantfiles = {}
counter = 0

for item in allfiles: 
    helper = item.split('.')
    if len(helper) > 1 and helper[1] == 'out':
        relevantfiles[counter] = item
        counter = counter +1

if counter == 1:
    filename = relevantfiles[0]
else:
    print 'These are the file that were found in the directory:'
    for i in relevantfiles:
        print str(i) + '...' + str(relevantfiles[i])
    number = int(raw_input('Please chose the number of the file you are interested in.\n')) 
    while number not in relevantfiles:
        number = int(raw_input('This number does not exist. \nPlease choose the correct number of the file you are interested in.\n'))
    filename = relevantfiles[number]
    
fnumber = 10 

f = open(filename,'r')
g = open('recovery values.csv','w+')

print str(filename) + ' is scanned.'

helpresult = []
counter = 0
countercells = 0
oil = 0
ratio = [0.149253731,0.022276676] # convert everything in relation to matrix cell!
special = range(1,112,11)

for line in f:
    text = line.split()
    if len(text) > 1:
        if text[0] == 'No.': # set it back
            helpresult.append(counter)
            print countercells
            counter = 0
            countercells = 0
        if text[0] == 'Oil' and text[1] == 'Saturation' and oil == 0: # start at oil
            oil = 1
        if text[0] == 'Gas' and text[1] == 'Saturation' and oil == 1: # end at gas
            oil = 0
        if oil == 1:
            if text[0] == 'Plane':
                if len(text) > 4 and text[4] == 'All': # whole plane at once only if length is enough (can be ignored as always zero/close to zero)
                    counter = counter + 111**2*float(text[7])
                    countercells = countercells + 111**2
            if text[0] == 'I': # save I-line
                if text[2] is not '99':
                    helper = range(int(text[2]),int(text[2])+14)
                else:
                    helper = range(99,111)
            if text[0] == 'J=': # standard J line
                if int(text[1]) in special: # whole line is fracture
                    for i in range(2,len(text)):                     
                        if int(helper[i-2]) in special:
                            counter = counter + float(text[i])*ratio[1] # fracture II
                            countercells = countercells + 1
                        else:
                            counter = counter + float(text[i])*ratio[0] # fracture I
                            countercells = countercells + 1
                else: # there is also matrix in this line
                    for i in range(2,len(text)):
                        if int(helper[i-2]) in special:
                            counter = counter + float(text[2])*ratio[0] # fracture I
                            countercells = countercells + 1
                        else:
                            counter = counter + float(text[2])          # matrix
                            countercells = countercells + 1
            if len(text[0]) > 2: # like J=100; this line: don't get an error message if text[0] too short
                if text[0][0] == 'J' and text[0][1] == '=' and text[0][2] == '1':
                    number = int(text[0][2]+text[0][3]+text[0][4])
                    if number in special: # whole line is fracture
                        for i in range(1,len(text)):                      
                            if int(helper[i-1]) in special:
                                counter = counter + float(text[i])*ratio[1] # fracture II
                                countercells = countercells + 1
                            else:
                                counter = counter + float(text[i])*ratio[0] # fracture I
                                countercells = countercells + 1
                    else: # there is also matrix in this line
                        for i in range(1,len(text)):
                            if int(helper[i-1]) in special:
                                counter = counter + float(text[i])*ratio[0] # fracture I
                                countercells = countercells + 1
                            else:
                                counter = counter + float(text[i])          # matrix
                                countercells = countercells + 1            
print helpresult
original = helpresult[0] # sat matrix * cells/block * layers in z * fnumber^2
print original
for i in helpresult:
    g.write(str((1 -i/original)*100) + '\n')

f.close()
g.close()
