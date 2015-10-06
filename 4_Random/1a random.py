import random
from writerrandom import writer
from writersector import writersector

numberfrac = 10                                                             # based on time analysis, can be changed 

percentage = raw_input('Please enter the percentage of fractures closed:')

percentage = int(percentage)

while percentage >= 100 or percentage <= 0:
    percentage = raw_input('Please enter the percentage of fractures closed.\nThe percentage needs to be an integer between 0 and 100!\n')
    percentage = int(percentage)

print percentage

allfractures = []

for i in range(0,numberfrac): # assume that only fractures in x and y are changed, therefore take 2 x numberfrac
    allfractures.append(1)
    allfractures.append(1)
    
numberclosed = int(numberfrac*percentage/50)
closed = []

while len(closed) < numberclosed:
    guess = random.randint(0,2*numberfrac-2)
    if guess not in closed:
        closed.append(guess)

for i in closed:
    allfractures[i+1] = 0

print allfractures

filename = 'output ' + str(percentage) + '.txt'

f = open(filename,'a+')

writersector(numberfrac,allfractures,filename)
writer('POR','0.2','0.0015',numberfrac,allfractures,filename)
writer('VOLMOD','1','1.0E+7',numberfrac,allfractures,filename)
writer('PERMI','10','15557',numberfrac,allfractures,filename)
writer('PERMJ','10','15557',numberfrac,allfractures,filename)
writer('PERMK','10','15557',numberfrac,allfractures,filename)
writer('RTYPE','1','2',numberfrac,allfractures,filename)
writer('SW','0.2','1',numberfrac,allfractures,filename)
writer('SO','0.8','0',numberfrac,allfractures,filename)

f.close()
