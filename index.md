## Description
Washing machine is a simple system whose operations can be emulated through software. The assembler assumes that the operations happening on the hardware level are implemented in the system itself. The assembler only converts the assembly level program to a binary output.
- The washing machine is a simple device consisting of two basic operations - **WASH** and **DRY**.
- All the instructions, sub-routines and operations are a part of the machine that facilitate the two basic operations.
- The system consists of a **timer** to control how long a task is executed, **temperature control** to decide the temperature during the wash cycle, **spin speed** and **wash type control** to decide machine's current state i.e. washing state or drying state.
- The **timer**, **temperature control**, **spin speed** and **wash type control** are all controlled by sub-routines which implement the above descirbed operations utilizing some reserved memory locations, predefined labels and values.

For information regarding the sytax of the assembly level program and further insight, please refer to the [project report](https://github.com/maanas-talwar/pywash/blob/main/Report.pdf).  
Find a sample program respecting the syntax rules [here](https://github.com/maanas-talwar/pywash/blob/main/assembler/sample.txt).

## Dependencies:
> Language: Python(3.8)

## Contents
* `./assembler` - contains the code for the 2 pass assembler
* `./assembler/hardcode.py` and `./assembler/Pass.py` are dependencies for the main program `./assembler/wash_assemble.py`
* `./assembler/sample.txt` and `./assembler/error_program.txt` are sample assembly programs
* `./assembler/mandatorySBR.txt` contains some mandatory subroutines that should be present at the end of the assembly program with user defined values for the declared variables
* `./assembler/sample.txt` - sample input
* `./assembler/sample_bin.txt` - sample output
* `./assembler/wash_assemble.py` - source code

## Execution
* To run the assembler, first change your directory to `pywash/assembler/` using the following command:
> cd pywash/assembler/
* Save the assembly level input program in this directory.
* The process can be run by the following command:
> python wash_assemble.py
* The output binary file named <program_name>_bin.txt can be found in the same directory.

## Results
The following results are as per the [sample input file](https://github.com/maanas-talwar/pywash/blob/main/assembler/sample.txt) and the binary output is available as [sample_bin.txt](https://github.com/maanas-talwar/pywash/blob/main/assembler/sample_bin.txt).  
![image](https://user-images.githubusercontent.com/54113320/131447911-12722c20-9bff-4882-b78a-bde30c03e468.png)  
![image](https://user-images.githubusercontent.com/54113320/131447944-3693557e-36f9-4791-8dbd-4942b592389f.png)

