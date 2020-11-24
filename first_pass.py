'''
        Purpose: To implement the first pass of a 2 pass assembler for a sample washing machine controller.
'''

allInstructions = ["STA", "LDA", "ISZ", "BSA", "BUN", "CLA", "CMA", "SRT", "STP",
                   "INC", "SZA", "ICL", "IST", "OCL", "OST", "INP", "SKI", "SPN", "HLT", "DRN"]

# all operands stored as "operand_name": "value"
operands = {}

# all labels stored as "label": "location_counter"
labels = {}

# no space between label and ':' or ','

if __name__ == '__main__':
    print('*****  First Pass Start *****')
    with open("sample.txt", "r") as file:
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
