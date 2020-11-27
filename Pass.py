from hardcode import *
import time
green = "\033[92m {}\033[00m"
allInstructions = ["STA", "LDA", "ISZ", "BSA", "BUN", "CLA", "CMA", "SRT", "STP",
                   "INC", "SZA", "ICL", "IST", "OCL", "OST", "INP", "SKI", "SPN", "HLT", "DRN"]

# all operands stored as "operand_name": "value"
operands = {}

# all labels stored as "label": "location_counter"
labels = {}

def pass1(name):
    #print('*****  First Pass Start *****')
    with open(name, "r") as file:
        # starting location counter at memory location 10
        lc = 10
        line = file.readline()
        while(line):
            # removing extra white spaces
            line = " ".join(line.split())
            probableLabel = line.split(" ", 1)[0]
            if(";" in probableLabel):
                probableLabel = probableLabel.split(";", 1)[0]

            if(probableLabel not in allInstructions and len(" ".join(probableLabel.split())) != 0):
                if(probableLabel.endswith(":")):
                    # dropped :
                    labels[probableLabel[:-1]] = lc
                elif(probableLabel.endswith(",")):
                    # dropped ','
                    probableLabel = probableLabel[:-1]
                    operands[probableLabel] = lc
            lc += 1
            line = file.readline()
        print("Operands:")
        print(operands)
        print("Labels:")
        print(labels)

    print(green.format('*****  First Pass End *****'))


def pass2(name):
    with open(name, "r") as file:
        outputFile = open(name[:-4]+"_bin.txt", "w")
        LocationCounter = 10
        line = file.readline()
        while(line):
            #line = " ".join(line.split())
            #line = line.replace(';', '')
            field = line.split()

            if line and line[0] > ' ' :
                #print(line)
                if field[0] == ';':
                    line = file.readline()
                    continue
                for i in range(0, len(field)):
                    if ';' in field[i]:
                        field[i] = field[i][:-1]
                        field = field[:i+1]
                        break

                while (',' in field):
                    field.remove(',')

                #print(field)

                if field and (field[0] in labels or field[0] in operands):
                    field = field[1:]
                if not field:
                    line = file.readline()
                    continue
                #try:
                if field[0] in MRI:
                    print(field)
                    Instruction = MRI[field[0]]
                    if(len(field)==3):
                        Instruction = '1'+MRI[field[0]][1:]
                    if field[1] != None:
                        Address = labels[field[1]] if field[1] in labels else operands[field[1]]
                        output = list()
                        output.append(bin(LocationCounter)[2:])
                        output.append(Instruction)
                        output.append(bin(int(Address))[2:].zfill(12))
                        outputFile.write(' '.join(map(str, output)))
                        outputFile.write('\n')
                    else:
                        #ERROR
                        outputFile.write("*****************")
                elif field[0] in REGREF:
                    print(field)
                    Instruction = REGREF[field[0]]
                    Address = ""
                    output = list()
                    output.append(bin(LocationCounter)[2:])
                    output.append(Instruction)
                    output.append(Address)
                    outputFile.write(' '.join(map(str, output)))
                    outputFile.write('\n')
                time.sleep(0.5)
                #print(LocationCounter, Instruction, Address)
                LocationCounter += 1
                #except:
                #    print ("exception")
            line = file.readline()
        outputFile.close()
        print(green.format('*****  Second Pass End *****'))

        print(green.format("The output file has been successfully generated as "+name[:-4]+"_bin.txt in your directory!"))

# if __name__ == "__main__":
#     pass1("sample.txt")
#     pass2("sample.txt")
