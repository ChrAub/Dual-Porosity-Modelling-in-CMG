import os

allfiles = os.listdir(os.getcwd())

for item in allfiles: # if there is only one .out-file in the directory it will be found
    helper = item.split('.')
    for word in helper:
        if word == 'out':
            filename = str(helper[0]) + '.' + 'out'

fnumber = int(filename.split()[2].split('.')[0]) # price for the most complex expression ever?

f = open(filename,'r')
g = open('recovery values.csv','w+')

print fnumber
print filename

helpresult = []
counter = 0
countercells = 0
oil = 0

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
            if text[0] == 'J=': # like J= 99
                for i in range(2,len(text)):
                    counter = counter + float(text[i])
                    countercells = countercells + 1
            if len(text[0]) > 2: # like J=100; this line: don't get an error message if text[0] too short
                if text[0][0] == 'J' and text[0][1] == '=' and text[0][2] == '1':
                    for i in range(1,len(text)):
                        counter = counter + float(text[i])
                        countercells = countercells + 1
print helpresult

# fix cell counter

original = 0.8*1000*3*fnumber**2 # sat matrix * cells/block * layers in z * fnumber^2

print original

for i in helpresult:
    g.write(str((1 -i/original)*100) + '\n')

f.close()
g.close()
