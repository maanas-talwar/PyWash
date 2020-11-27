allInstructions = ["STA", "LDA", "ISZ", "BSA", "BUN", "CLA", "CMA", "SRT", "STP",
                   "INC", "SZA", "ICL", "IST", "OCL", "OST", "INP", "SKI", "SPN", "HLT", "DRN"]

MRI = {'STA': '0000','LDA':'0001','ISZ':'0010','BSA':'0011','BUN':'0100'}
REGREF = { 'SRT':'','STP':'','SPN':'','HLT':'','ICL':'',
    'IST':'','OCL':'','OST':'','CLA':'','CMA':'','INC':'','SZA':''}

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
                    labels[probableLabel[:-1]] = lc
                elif(probableLabel.endswith(",")):
                    # dropped ','
                    probableLabel = probableLabel[:-1]
                    lineValues = line.split(" ")
                    value = lineValues[2]
                    if(lineValues[1].upper() == "HEX"):
                        # convert to binary
                        binaryValue = bin(int(value, 16))[2:].zfill(12)
                    elif(lineValues[1].upper() == "DEC"):
                        # convert to binary
                        binaryValue = bin(int(value, 10))[2:].zfill(12)

                    operands[probableLabel] = binaryValue

            lc += 1
            line = file.readline()
        print("Operands:")
        print(operands)
        print("Labels:")
        print(labels)

    print('*****  First Pass End *****')


def pass2(name):
    with open(name, "r") as file:
        outputFile = open("OutputFile.txt", "w")
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
                    if field[1] != None:
                        Address = labels[field[1]] if field[1] in labels else operands[field[1]]
                        output = list()
                        output.append(bin(LocationCounter))
                        output.append(Instruction)
                        output.append(Address)
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
                    output.append(bin(LocationCounter))
                    output.append(Instruction)
                    output.append(Address)
                    outputFile.write(' '.join(map(str, output)))
                    outputFile.write('\n')

                #print(LocationCounter, Instruction, Address)
                LocationCounter += 1
                #except:
                #    print ("exception")
            line = file.readline()
        outputFile.close()
        print('*****  Second Pass End *****')

# if __name__ == "__main__":
#     pass1("sample.txt")
#     pass2("sample.txt")