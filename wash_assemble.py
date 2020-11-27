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
name = input("Enter file name with extension :")
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
        #print(program)

        # condition 1
        condition1 = 0
        if program[0] == 'SRT':
            print("No start error")
            condition1 = 1
        else:
            print(RED.format("Program is not started by SRT"))
        # condition 2
        condition2 = 1
        for i in program:
            if(i == 'STP'):
                break
            c = 0
            for j in i:
                if j == " ":
                    c = c+1
            if(c > 2):
                print(RED.format("Line \"", i, "\" has more than 3 fields"))
                condition2 = 0
                break
        if condition2 == 1:
            print("No syntax error")

        # condition 3
        condition3 = 0
        address = set()
        for i in program:
            if(i == 'STP'):
                eof = program.index(i)
                break
            if(i[0:3] in MRI):
                address.add(i[4:8].split(' ')[0]) if i[4:8] not in address else address
        check = set()
        for i in program:
            check.add(i.split(',')[0].split(" ")[0])
            check.add(i.split(':')[0].split(" ")[0])
        condition3 = 1 if all(i.split(',')[0].split(
            " ")[0] in address.union(MRI) for i in program) else 0
        condition3 = 1 if address.union(MRI).difference(check) == {''} else 0
        print("No labelling error") if condition3 == 1 else print(
            "You missed some labels: ", address.union(MRI).difference(check))

        # condition 4
        condition4 = 0
        labels = []
        reserved = {'TM', 'TP', 'SPD', 'WT', 'CLN'}
        for i in program[eof+1:len(program)]:
            if ',' in i and i.split(',')[0].split(" ")[0] not in reserved:
                labels.append(i.split(',')[0].split(" ")[0])

        if(len(labels) != len(set(labels))):
            print(RED.format("Your labels contain duplicate names "))
        else:
            print("No naming error")
            condition4 = 1

        # condition 5 and 6
        condition5 = 1
        condition6 = 1
        for i in program:
            if i[0:3] in MRI:
                if len(i) != 3:
                    continue
                else:
                    print(RED.format("MRI error at line containing", i))
                    condition5 = 0
                    break
            else:
                if ',' in i:
                    continue
                else:
                    if len(i) != 3:
                        print(RED.format("Non-MRI error at line containing", i))
                        condition6 = 0
                        break
        if condition5 == 1:
            print("No MRI error")
        if condition6 == 1:
            print("No non-MRI error")
        # syntax analysis
        for i in address:
            if i[0].isnumeric() or len(i) > 3 or '.' in i:
                print(i, "is an invalid address")

        #Two pass assembly
        print(GREEN.format("Correct program!\nTranslating..."))
        Pass.pass1(name)
        Pass.pass2(name)
    else:
        print(RED.format(ext + " extension not suppported.\nPlease enter a file with extensions .txt or .asm"))
else:
    print(RED.format("Please enter valid file name"))
