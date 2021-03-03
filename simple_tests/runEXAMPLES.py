# alterative to sh script (first pass)
# $ python runEXAMPLES.py f77/
import sys
import os

dryrun=True
writetodir = True
debug=False

if len(sys.argv) == 1:
    direct = './'
else:
    direct = sys.argv[1]

try:
    f = open(direct + 'EXAMPLES.f', 'r')
except:
    try:
        f = open(direct + 'EXAMPLES.f90','r')
    except:
        raise FileNotFoundError

separate='!#######################################################################\n'
start =  '!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
end =    '!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'

if debug: deb = open('debug.txt', 'w')

prevline = ''
line = f.readline()
if debug: deb.write(str(line))
example_num = 0
while(True): # loop over code blocks
    if line is None:
        continue
    if line == '':
        break
    elif line == '\n' and prevline == separate:
        example_num += 1
        filenames = []
        while(True): # loop over files in code block
            if line == '':
                break
            elif line == separate:
                break
            elif line[:2] =='!$':
                if dryrun:
                    print('runbash:'+line[2:-1])
                else:
#cd doesnt change directory any further os.system calls are in, so this needs to be done in one line
                    os.system('cd %s && %s'%(direct,line[2:-1]))
            elif line == start:
                filename = prevline[1:-1]
                filenames.append(filename)

                prevline = line
                line = f.readline()
                if debug: deb.write(str('c\n'))

                filelines = []
                while(True): # look over lines in file
                    prevline = line
                    line = f.readline()
                    if debug: deb.write(str('d\n'))

                    filelines.append(prevline)
                    if line == end:
                        break

                if writetodir:
                    exdirect = direct + 'example%d/'%(example_num)
                    if not os.path.exists(exdirect): os.makedirs(exdirect)
                    with open(exdirect + filename, 'w') as g:
                        g.write(''.join(filelines))

                if dryrun: 
                    print(str('filename = '+str(filename)))
                    #print(str('filelines = '+str(filelines)))
                    print(direct + 'example%d/'%(example_num) + filename)
                else:
                    with open(direct + filename, 'w') as g:
                        g.write(''.join(filelines))

            prevline = line
            line = f.readline()
            if debug: deb.write(str('b\n'))

        filenames.append('a.out') # due to extra separators at end of EXAMPLES file, this add an extra time for last example
        for filename in filenames:
            if dryrun:
                print('remove '+direct+filename)
            else:
                os.system('rm '+direct+filename)

    prevline = line
    line = f.readline()
    if debug: deb.write(str('a\n'))
