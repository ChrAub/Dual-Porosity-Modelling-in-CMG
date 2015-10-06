def writersector(numberfrac, allfractures, filename): # writes a generic sets of units for a CMG input file
    f = open(filename, 'a')

    for i in range(0,numberfrac): # x direction
        helper = 1 + i*11
        if allfractures[i] == 1: # write fracture
            f.write('SECTOR \'fractures\' 1:111 ' + str(helper) + ':' + str(helper) + ' 1:34\n')

    f.write('\n')
        
    for i in range(numberfrac, 2*numberfrac): # y direction
        helper = 1 + (i-numberfrac)*11
        if allfractures[i] == 1: # write fracture
            f.write('SECTOR \'fractures\' ' + str(helper) + ':' + str(helper) + ' 1:111 1:34\n')

    f.write('\n')

