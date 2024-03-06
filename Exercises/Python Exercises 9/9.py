import os
#Ask the user for the name of two input files. 
#If some of them don’t exist, display an error message and exit. 
f1 = input('First input file: ')
if not os.path.exists(f1):
    print('Error: file', f1, 'not found')
    exit()
f2 = input('Second input file: ')
if not os.path.exists(f2):
    print('Error: file', f2, 'not found')
    exit()
#Ask the user for the name the output file. If it exists, display a warning
#message and ask the user for overwriting the file or exit.
f3 = input('Output file: ')
if os.path.exists(f3):
    opc = input('Warning: file {} exists, overwrite? (Y/N): '.format(f3))
    if opc.lower() != 'y':
        exit()
#Using a while loop and the method readline(), read the input files line by line
#and write them into the output file in such a way that it is ordered too. 
#Do not use any kind of array.
fin1 = open(f1, 'r')
fin2 = open(f2, 'r')
fout = open(f3, 'w')
line1 = fin1.readline()
line2 = fin2.readline()
while line1 or line2:
    if not line2 or line1 and line1 <= line2:
        fout.write(line1)
        line1 = fin1.readline()
    else: 
        fout.write(line2)
        line2 = fin2.readline()
fin1.close()
fin2.close()
fout.close()