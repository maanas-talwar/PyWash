    # Defining the hardcodes of the instructions present in our system
    # MRI-> Memory reference
    # REGREF -> Register reference
    # IO -> Input/ output
    # PSEUDO -> Pseudo instructions
MRI = {'STA': '0000','LDA':'0001','ISZ':'0010','BSA':'0011','BUN':'0100'}
REGREF = { 'CLA':'','CMA':'','INC':'','SZA':'','ICL':'','IST':'',
    'OCL':'','OST':'','SPN':'','HLT':'','SRT':'','STP':''}
# Generating the opcodes
seven = '1111'
counter = 1<<11
zeroes = ""
for a,b in REGREF.items():
    binary = str(bin(counter))[2:]
    REGREF[a] = seven+zeroes+binary
    zeroes+= '0'
    counter = counter>>1
IO = {'INP':'1111100000000000','SKI':'1111010000000000'}
# print("Memory Reference :",MRI)
# print()
# print("Register Reference :",REGREF)
# print()
# print("Input / output :",IO)
# starting the assembly process
name = input("Enter file name with extension :")
if(len(name.split('.'))==2):
    ext = name[-3:]
    # Checking the extension for the file
    if(ext=="txt" or ext=="asm"):
        try:
            file = open(name,'r+')
            # append code here -> aryaman.
        except:
            print("Error in opening",name,"\nPlease check its availability in your current directory.")
    else:
        print(ext,"extension not suppported.\nPlease enter a file with extensions .txt or .asm")
else:
    print("Please enter valid file name")
