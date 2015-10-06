def writerbig(name, valuem, valuef, helper, namefile): # writes a generic sets of units for a CMG input file

    f = open(namefile,'a')
    
    number = helper/11 - 1
    fracsets = [1]
    for i in range(1,number+2):
        fracsets.append(1+i*11)

    f.write(name + ' IJK\n')
    f.write('1:' + str(helper) + ' 1:' + str(helper) + ' ' + '1:34 ' + valuem + '\n')                                             
    f.write('1:' + str(helper) + ' 1:' + str(helper) + ' ' + '1:1 ' + valuef + '\n')
    f.write('1:' + str(helper) + ' 1:' + str(helper) + ' ' + '12:12 ' + valuef + '\n')
    f.write('1:' + str(helper) + ' 1:' + str(helper) + ' ' + '23:23 ' + valuef + '\n')
    f.write('1:' + str(helper) + ' 1:' + str(helper) + ' ' + '34:34 ' + valuef + '\n')
    f.write('\n')

    for i in range(0, number+2): # x direction
        f.write('1:' + str(helper) + ' ' + str(fracsets[i]) + ':' + str(fracsets[i]) + ' ' + '1:34 ' + valuef + '\n')

    f.write('\n')

    for i in range(0, number+2): # y direction
        f.write(str(fracsets[i]) + ':' + str(fracsets[i]) + ' ' + '1:' + str(helper) + ' ' +  '1:34 ' + valuef + '\n')    
        
    f.write('\n')

    if name == 'PERMK':
        f.write('\n')
        f.write('MIDDLE REACHED\n')
        f.write('\n')

    if name == 'RTYPE':
        f.write('INITIAL\n')
        f.write('USER_INPUT\n')
        f.write('PRES CON 20000\n')

