import os

allfiles = os.listdir(os.getcwd())

for item in allfiles: # if there is only one .out-file in the directory it will be found
    helper = item.split('.')
    for word in helper:
        if word == 'out':
            filename = str(helper[0]) + '.' + 'out'
            
f = open(filename,'r')
g = open('recovery values.csv','w+')

oil = 0

for line in f:
    text = line.split()
    if len(text) > 1: # eliminate empty lines
        if text[0] == 'Oil' and text[1] == 'Saturation':
            oil = 1
        if text[0] == 'Fundamental' and text[1] == 'Grid' and text[3] == 'Fracture':
            oil = 0
        if oil == 1 and text[1] == 'All':
            print 'yes'
            g.write(str(100*((1-float(text[4])/0.8))) + '\n')
        

f.close()
g.close()
