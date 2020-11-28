MRI = {'STA': '0000','LDA':'0001','ISZ':'0010','BSA':'0011','BUN':'0100'}
REGREF = { 'SRT':'','STP':'','SPN':'','HLT':'','ICL':'',
    'IST':'','OCL':'','OST':'','CLA':'','CMA':'','INC':'','SZA':''}
# Generating the opcodes
seven = '0111'
counter = 1 << 11
zeroes = ""
for a, b in REGREF.items():
    binary = str(bin(counter))[2:]
    REGREF[a] = seven+zeroes+binary
    zeroes += '0'
    counter = counter >> 1
REGREF['LCK'] = '0111000000000000'
IO = {'SKI': '1111100000000000', 'INP': '1111010000000000'}
# print(MRI)
# print(REGREF)
