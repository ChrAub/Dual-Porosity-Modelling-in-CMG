f = open('3 all the rest random 2.txt','r+') #input
g = open('sat.txt','r+') #input
h = open('gasinj.dat','w+') #output

first = 1
second = 0

for line in g: # get dimensions of model
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'dim':
            x = text[1]
            y = text[2]
            z = text[3]
            break

for line in f: # first part
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == 'CHANGE':
            first = 0
        if first == 1 and text[0] == 'GRID' and text[1] == 'VARI':
            h.write('GRID VARI ' + x + ' ' + y + ' ' + z + '\n')
        elif first == 1:
            h.write(line)
        else:
            a = 5
f.close()

water = 0

for line in g:
    text = line.split()
    if len(text) > 0: # ignore empty lines
        if text[0] == '34' and text[1] == '34' and text[2] == '34' and water == 0: # write oil 
            water = 1            
            h.write(line)
            h.write('\n')
            h.write('1:34 1:34 1:1   0\n')
            h.write('1:34 1:34 12:12 0\n')
            h.write('1:34 1:34 23:23 0\n')
            h.write('1:34 1:34 34:34 0\n')
            h.write('1:34 1:1 1:34   0\n')
            h.write('1:34 12:12 1:34 0\n')
            h.write('1:34 23:23 1:34 0\n')
            h.write('1:34 34:34 1:34 0\n')
            h.write('1:1 1:34 1:34   0\n')
            h.write('12:12 1:34 1:34 0\n')
            h.write('23:23 1:34 1:34 0\n')
            h.write('34:34 1:34 1:34 0\n')            
        elif text[0] == '34' and text[1] == '34' and text[2] == '34' and water == 1: # write water
            h.write(line)
            h.write('\n')
            h.write('1:34 1:34 1:1   0\n')
            h.write('1:34 1:34 12:12 0\n')
            h.write('1:34 1:34 23:23 0\n')
            h.write('1:34 1:34 34:34 0\n')
            h.write('1:34 1:1 1:34   0\n')
            h.write('1:34 12:12 1:34 0\n')
            h.write('1:34 23:23 1:34 0\n')
            h.write('1:34 34:34 1:34 0\n')
            h.write('1:1 1:34 1:34   0\n')
            h.write('12:12 1:34 1:34 0\n')
            h.write('23:23 1:34 1:34 0\n')
            h.write('34:34 1:34 1:34 0\n')
        else:
            h.write(line)          

f = open('3 all the rest random 2.txt','r+') #input

for line in f:
    text = line.split()
    if len(text) > 0:
        if second == 1:
            h.write(line)
        if text[0] == 'CHANGE':
            second = 1

f.close()
g.close()
h.close()
