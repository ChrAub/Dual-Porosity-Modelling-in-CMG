import os

allfiles = os.listdir(os.getcwd())

for item in allfiles: # if there is only one .out-file in the directory it will be found
    helper = item.split('.')
    for word in helper:
        if word == 'out':
            filename = str(helper[0]) + '.' + 'out'

print filename + ' has been scanned.'

f = open(filename,'r')
g = open('cut.txt','w+')

cut = 1

#time = raw_input("Please enter time of last timestep. \nThe default value is 50.00. \n")
#print 'The last timestep is defined to be ' + time + '.'

# finds automatically last timestep and cuts everything above it

time = 0

for line in f:
    text = line.split()
    if len(text) > 1 and text[0] == 'Time' and text[3] == '**********************************************************************':
        time = text[2]
print time

f.close()
f = open(filename,'r')

for line in f:
    text = line.split()
    if len(text) > 1:
        if text[0] == 'GRID' and text[1] == 'VARI':
            g.write('dim ' + text[2]+ ' ' + text[3] + ' ' + text[4] + '\n')
        if text[0] == 'Time' and text[1] == '=' and text[2] == str(time) and cut == 1:
            cut = 0
        if cut == 0:
            g.write(line)

f.close()
g.close()
