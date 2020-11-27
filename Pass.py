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
        # print("Operands:")
        # print(operands)
        # print("Labels:")
        # print(labels)

    #print('*****  First Pass End *****')


def pass2(name):
    with open(name, "r") as file:
        outputFile = open("OutputFile.txt", "w")
        LocationCounter = 10
        line = file.readline()
        while(line):
            line = " ".join(line.split())
            field = line.split(" ", 1)[0]
            if(";" in field):
                field = field.split(";", 1)[0]

            if line[0] > ' ' :
                if(field.endswith(":") or field.endswith(",")):
                    # dropped ':' and ','
                    field = field[:-1]

                if field and field[0] in labels:
                    field = field[1:]
                if not field:
                    continue
                try:
                    if field[0] in MRI:
                        Instruction = MRI[field[0]]
                        if field[1] != None:
                            Address = labels[field[1]] if (field[1] in labels) else operands[field[1]]
                            outputFile.write(LocationCounter, Instruction, Address)
                        else:
                            #ERROR
                            outputFile.write("*****************")
                    elif field[0] in REGREF:
                        Instruction = REGREF[field[0]]
                        Address = ""
                        outputFile.write(LocationCounter, Instruction, Address)

                    #print(LocationCounter, Instruction, Address)
                    LocationCounter += 1
                    line = file.readline()
                except:
                    print ("******************")
        outputFile.close()
