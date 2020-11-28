import Pass
# Defining the hardcodes of the instructions present in our system
# MRI-> Memory reference
# REGREF -> Register reference
# IO -> Input/ output
# PSEUDO -> Pseudo instructions
from hardcode import *
# print("Memory Reference :",MRI)
# print()
# print("Register Reference :",REGREF)
# print()
# print("Input / output :",IO)
# starting the assembly process
GREEN = "\033[92m {}\033[00m"
RED = "\033[91m {}\033[00m"
name = input("\nEnter file name with extension :")
if(len(name.split('.')) == 2):
    ext = name[-3:]
    # Checking the extension for the file
    if(ext == "txt" or ext == "asm"):
        try:
            file = open(name, 'r+')
        except:
            print(RED.format("Sorry, the file wasn't found. Please check directory for the given file"))
            exit()
        program = file.readlines()
        #print(program)
        program = [' '.join(i.split(";", 1)[0].split()) for i in program]
        program = [i.upper() for i in program if i]
        print(program)
        condition = [0, 1, 0, 0, 1, 1]
        if program[0] == 'SRT':
            print(GREEN.format("No start error"))
            condition[0] = 1
        else:
            print(RED.format("Program is not started by SRT"))
        # condition 2
        for i in program:
            if(i == 'STP'):
                break
            c = 0
            for j in i:
                if j == " ":
                    c = c+1
            if(c > 2):
                print(RED.format("Line \""+str(i)+ "\" has more than 3 fields"))
                condition[1] = 0
                break
        if condition[1] == 1:
            print(GREEN.format("No syntax error"))

            # condition 3
        address = set()
        for i in program:
            if(i == 'STP'):
                eof = program.index(i)
                break
            if(i[0:3] in MRI):
                address.add(i[4:8].split(' ')[0]) if i[4:8] not in address else address
        labels = set()
        mandatory = set()
        file2 = open('mandatorySBR.txt', 'r')
        program2 = file2.readlines()
        for i in program2:
            if ',' in i:
                mandatory.add(i.split(',')[0])
            if ':' in i:
                mandatory.add(i.split(':')[0])
        for i in program:
            if ':' in i:
                labels.add(i.split(':')[0]) if i.split(':')[0] not in labels else labels
            if ',' in i:
                labels.add(i.split(',')[0]) if i.split(',')[0] not in labels else labels
        condition[2] = 1 if address.difference(labels) == set(
        ) and mandatory.difference(address) == set() else 0
        print(GREEN.format("No labelling error")) if condition[2] == 1 else print(RED.format("You missed some labels: "+str(
                                                                    (address.difference(labels)).union(mandatory.difference(address)))))

        # condition 4
        if(len(labels) != len(set(labels))):
            print(RED.format("Your labels contain duplicate names "))
        else:
            print(GREEN.format("No naming error"))
            condition[3] = 1

        # condition 5 and 6
        for i in program:
            if i[0:3] in MRI:
                if len(i) != 3:
                    continue
                else:
                    print(RED.format("MRI error at line containing "+str(i)))
                    condition[4] = 0
                    break
            elif i[0:3] in REGREF or i[0:3] in ['SKI', 'INP']:
                if len(i) == 3:
                    continue
                else:
                    print(RED.format("Non-MRI error at line containing "+str(i)))
                    condition[5] = 0
                    break
            else:
                if ',' in i or ':' in i:
                    continue
                else:
                    print(RED.format("Undefined field at line containing "+str(i)))
                    condition[5] = 0
                    break
        if condition[4] == 1:
            print(GREEN.format("No MRI error"))
        if condition[5] == 1:
            print(GREEN.format("No non-MRI error"))
        # syntax analysis
        for i in address:
            if i[0].isnumeric() or len(i) > 3 or '.' in i:
                print(RED.format(str(i)+ "is an invalid address"))

        if all(i == 1 for i in condition):
            # Two pass assembly
            print(GREEN.format("Correct program!\nTranslating..."))
            Pass.pass1(name)
            Pass.pass2(name)
        else:
            print(RED.format("Please rectify the above error(s) before proceeding further"))
    else:
        print(RED.format(ext + " extension not suppported.\nPlease enter a file with extensions .txt or .asm"))
else:
    print(RED.format("Please enter valid file name"))
