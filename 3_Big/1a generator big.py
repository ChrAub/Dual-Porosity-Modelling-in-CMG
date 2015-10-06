import random
from writerbig import writerbig
       
number = raw_input('Please enter the number of fracture sets in x and y direction:\n')
number = int(number) # number fracture cells
helper = 1+number*11 # number cells

name = 'medium.' + str(number) + '.txt' # name of file
f = open(name,'w+')

f.write('GRID VARI ' + str(1+number*11) + ' ' + str(helper) + ' 34\n')
f.write('KDIR DOWN\n')
f.write('DI IVAR\n')
f.write('0.01 ')
for i in range(0,number):
    f.write('10*0.067 0.01 ')
f.write('\n')
f.write('DJ JVAR\n')
f.write('0.01 ')
for i in range(0,number):
    f.write('10*0.067 0.01 ')
f.write('\n')
f.write('DK KVAR\n')
f.write(' 0.01 10*0.067 0.01 10*0.067 0.01 10*0.067 0.01\n')
f.write('DTOP\n')
f.write(str(helper**2) + '*1000\n')
f.write('\n')
f.close()

f = open(name,'a')
writerbig('POR','0.2','0.0015',helper,name)
writerbig('VOLMOD','1','1.0E+7',helper,name)
writerbig('PERMI','10','15557',helper,name)
writerbig('PERMJ','10','15557',helper,name)
writerbig('PERMK','10','15557',helper,name)
writerbig('RTYPE','1','2',helper,name)
writerbig('SW','0.2','1',helper,name)
writerbig('SO','0.8','0',helper,name)
f.close()
