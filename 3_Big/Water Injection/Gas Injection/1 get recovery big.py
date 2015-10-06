import os

allfiles = os.listdir(os.getcwd())

for item in allfiles: # if there is only one .out-file in the directory it will be found
    helper = item.split('.')
    for word in helper:
        if word == 'out':
            filename = str(helper[0]) + '.' + 'out'
            
f = open(filename,'r')
g = open('recovery values gas.csv','w+')

relevant = []

for line in f:
    text = line.split()
    if len(text) == 10 and text[3] == '0':
        number = text[0]
        if number[len(number)-1] == 'w':
            relevant.append(1)
        else:
            relevant.append(0)

print relevant

f.close()
f = open(filename,'r')

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
                    counter = counter + 34**2*float(text[7])
                    countercells = countercells + 34**2
            if text[0] == 'J=':
                for i in range(2,len(text)):
                    counter = counter + float(text[i])
                    countercells = countercells + 1
print helpresult

#for i in range(0,len(relevant)):
#    if relevant[i] == 1:
#        result.append(helpresult[i])

for i in helpresult:
    g.write(str((1 -i/27000/0.8)*100) + '\n')

f.close()
g.close()
