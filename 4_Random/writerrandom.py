def writer(name, valuem, valuef, numberfrac, allfractures, filename): # writes a generic sets of units for a CMG input file
    f = open(filename, 'a')

    f.write(name + ' IJK\n')
    f.write('1:111 1:111 1:34 ' + valuem + '\n')     # matrix                                             
    f.write('1:111 1:111 1:1 ' + valuef + '\n')     # fractures
    f.write('1:111 1:111 12:12 ' + valuef + '\n')
    f.write('1:111 1:111 23:23 ' + valuef + '\n')
    f.write('1:111 1:111 34:34 ' + valuef + '\n')
    f.write('\n')

    for i in range(0,numberfrac): # x direction
        helper = 1 + i*11
        if allfractures[i] == 1: # write fracture
            f.write('1:111 ' + str(helper) + ':' + str(helper) + ' 1:34 ' + valuef + '\n')

    f.write('\n')
        
    for i in range(numberfrac, 2*numberfrac): # y direction
        helper = 1 + (i-numberfrac)*11
        if allfractures[i] == 1: # write fracture
            f.write(str(helper) + ':' + str(helper) + ' 1:111 1:34 ' + valuef + '\n')

    f.write('\n')

    if name == 'PERMK':
        f.write('\n')
        f.write('MIDDLE REACHED\n')
        f.write('\n')

    if name == 'RTYPE':
        f.write('INITIAL\n')
        f.write('USER_INPUT\n')
        f.write('PRES CON 20000\n')
