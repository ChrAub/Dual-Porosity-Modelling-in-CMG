f = open('cut.txt','r')
g = open('sat.txt','w+')

# x blocks in k
# y blocks in i
# z blocks in j

oil = 0
gas = 0

# find dimensions

for line in f:
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'dim':
            x = int(text[3])
            y = int(text[1])
            z = int(text[2])  

f.close()

#set data structure k,i,j

oilsat = {}
watersat = {}
gassat = {}

for i in range(1,x+1):
    oilsat[i] = {}
    watersat[i] = {}
    gassat[i] = {}

for i in range(1,x+1):
    for j in range(1,y+1):
        oilsat[i][j] = {}
        watersat[i][j] = {}
        gassat[i][j] = {}

for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
            oilsat[i][j][k] = 0
            watersat[i][j][k] = 0
            gassat[i][j][k] = 0

# read input file

f = open('cut.txt','r')

for line in f:
    text = line.split()
    if len(text) > 0: # ignore empty lines      
        if text[0] == 'Oil' and text[1] == 'Saturation' and oil == 0: # what section of the text are you in?
            oil = 1
            gas = 0
        if text[0] == 'Gas' and text[1] == 'Saturation' and oil == 1 and gas == 0:
            oil = 0
            gas = 1
        if text[0] == 'Water' and text[1] == 'Saturation':
            oil = 0
            gas = 0
        if text[0] == 'Plane': #define plane
            K = int(text[3])
            if len(text) > 4 and text[4] == 'All': # check if all values in the plane are the same, works
                allvalues = float(text[7])
                for i in range(1,y+1): # set them to this value
                    for j in range(1,z+1):
                        if oil == 1:
                            oilsat[K][i][j] = float(allvalues)
                        if gas == 1:
                            gassat[K][i][j] = float(allvalues)
        if text[0] == 'I': #define i dimension
            if text[2] == '1':
                I = range(1,15)
            elif text[2] == '15':
                I = range(15,29)
            else:
                I = range(29,35)
        if text[0] == 'J=': #take data, decide length before
            counter = 1
            for i in I:
                if oil == 1:
                    oilsat[K][i][int(text[1])] = float(text[counter+1])
                if gas == 1:
                    gassat[K][i][int(text[1])] = float(text[counter+1])
                counter = counter + 1
            
# calculate watersaturation = 1 - oilsaturation - gassaturation      

for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
            watersat[i][j][k] = 1 - oilsat[i][j][k] - gassat[i][j][k]

# write code for CMG

g.write('dim ' + str(y) + ' ' + str(z) + ' ' + str(x) + '\n')

oilamount = 0

g.write('SO IJK \n')
for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
            g.write(str(k)+' ' + str(j) + ' ' + str(i) + ' ' + str(oilsat[i][j][k])+ '\n')
            oilamount = oilamount + oilsat[i][j][k]
g.write('\n')

g.write('SW IJK \n')
for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
            g.write(str(k)+' ' + str(j) + ' ' + str(i) + ' ' + str(watersat[i][j][k])+ '\n')
            
f.close()
g.close()


print 1 - oilamount/(27000*0.8) # recovery factor for very last step, how to ensure ST (there is no formation factor?)


