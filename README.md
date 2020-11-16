# Two-Pass Assembler for a Washing Machine System - Computer Organization(CEECC07)
This is a project which aims to build a **Two-Pass Assembler for a real world system.**
### Team Members 
- Maanas Talwar - Roll No: 2019UCO1580
- Anav Chaudhary - Roll No: 2019UCO1577
- Aryaman Sharma - Roll No: 2019UCO1508
- Harshit Gupta - Roll No: 2019UCO1580
## Objective 
- To create a two-pass assembler for a washing machine system which produces a binary output for a task to be executed on it.
- Washing machine is a simple system whose operations can be emulated through software. In our assembler, it is asumed that the operations happening on the hardware level are implemented in the system itself and what we provide is a binary translated output of the provided assembly level program.

## Installation and Usage
1. Prerequisites - *python3, git bash(optional)*

2. Download the ``wash_assemble.py`` to a directory where you wish to store your assembly programs or you can run ``git clone https://github.com/TheGupta2012/CAOproject.git`` if you have git CLI installed in your system and ``cd CAOproject`` after the cloning process is done.

3. Open a terminal(linux/macOS) /command prompt(Windows) and navigate to the directory in which you downloaded the ``wash_assemble.py`` file.

4. It is advised to write or save your assembly program in the same directory as your ``wash_assemble.py`` file. An assembly file can have any extension which is (.txt or .asm).

5. Run the assembler program by typing ``python3 wash_assemble.py``

6. After the execution of the above command, you will be prompted to type in the name your assembly file. NOTE - please provide the exact path if the file is not in the smae directory as the assembler code.

7. If the assembly code is valid, you should see a message ``SUCCESSFULLY CONVERTED filename TO filename_binary.bin `` and a file with the name ``filename_binary.bin`` should be available for you to see in the same directory as the assembler file.

8. If there are any kinds of errors or warnings(discussed later) encountered during the assembling process, the CLI would show a ``ERROR ENCOUNTERED WHILE ASSEMBLING filename.asm. Please check message_filename.log for details.`` message. This means that whatever errors or warnings were encountered in the building of the binary file are recorder in the .log file with time stamping and line detection.

## Structure of our System
- Our washing machine is a simple device consisting of two basic operations - **WASH** and **DRY**. 

- All the instructions, sub-routines and operations are a part of the machine that facilitate the two basic operations.

- Our system consists of a **timer** which controls how long a task has to be executed, **temperature control** which decides at which temperature the wash cycle operates, **spin speed** defines the speed at which the clothes are spun in the machine and **wash type control** which decides whether the machine is in washing phase or the drying phase.

- The **timer**, **temperature control**, **spin speed** and **wash type control** are all controlled by sub-routines which implement the above descirbed operations, with some reserved memory locations, predefined labels and predefined values which correspond to a particular state of *temperature, spin speed and wash type*. The details of them are described further in the ISA of the machine.

## Instruction Set Architecture(ISA), Sub-routines and Reserved locations
### ISA
- ``16-bit architecture`` has been chosen for our instructions and a ``12-bit , word addressable memory `` is used for the storage of our instructions and operands.

<img src= "https://github.com/TheGupta2012/CAOproject/blob/main/instruction_format.JPG" width = 400px>

- The instructions used in our system are preceded by an addresssing mode bit which specifies *indirect* or *direct* addressing for our memory 

- The instructions available are divided into three parts - *Register Reference, Memory Reference and Input Output* instructions 

- The system has all the basic instructions that are required in any kind of processing unit and contains the registers which are mentioned below. A point to note is that there exists a special STATUS REGISTER which actually tells the system what it is doing at the moment.
  - `AC` - Accumulator - 16bit
  - `DR` - Data register - 16bit
  - `PC` - Program counter - 12bit
  - `AR` - Adress register - 12bit
  - `INPR` - Input Register - 8bit
  - `OUTR` - Output Register - 8bit
  - `SR` - Status register - 8bit (extra bits provided for future changes in functionality)
  
      <img src = "https://github.com/TheGupta2012/CAOproject/blob/main/status_register.JPG" width = 400px>
 
- **Instruction Set** : The instructions are based on the *Single Address Instruction* format and has the accumulator as the general purpose register. X referred to in the instructions is either a memory location or a symbolic address present as a label in the program.
  - `STA X` : Store value of AC directly in X or the location whose address is stored in X.
  - `LDA X` : Load the value of X directly or indirectly into AC.
  - `ISZ X` : Increment X and the skip the next instruction if X is zero
  - `BSA X` : Save return address in X and branch to the effective address of the subroutine.
  - `BUN X` : Branch unconditionally to X
  - `CLA`   : Clear AC , takes no operands
  - `CMA`   : Complement AC , takes no operands
  - `SRT`   : Start the execution of the machine , takes no operands
  - `STP`   : Stop the execution of the machine , takes no operands
  - `INC`   : Increment AC , takes no operands 
  - `SZA`   : Skip next instruction if AC is zero , takes no operands
  - `ICL`   : Clear inlet flag( inlet valve closed) , takes no operands
  - `ICS`   : Set inlet flag ( inlet valve open) , takes no operands
  - `OCL`   : Clear outlet flag ( outlet valve closed) , takes no operands
  - `OCS`   : Set outlet flag ( outlet valve open) , takes no operands
  - `INP`   : Input 8bit information and clear input flag , takes no operands
  - `SKI`   : Skip if input flag is set , takes no operands
  - `SPN`   : Spinning the motor of the machine before a wash cycle(sets motor flag to 1), takes no operands
  - `HLT`   : Halt motor (sets motor flag to 0), takes no operands 
  - `STP`   : Halt execution of washing machine, takes no operands
  
- **Sub-Routines** : The sub-routines for the **timing , wash-type, temperature and spin speed** are presented in this section. Note that these sub-routines refer to some predefined memory locations which are mentioned in the *Reserved Locations* section. We are presenting the software implementations of a program for a washing-machine cycle and thus the values associated with the different settings are input through *external switches* which indeed have representations of the values provided. The character input by the user is actually transferred in the `INPR` and then to the required memory locations in the internal executions of these subroutines.

  - `TIM` : Setting the timer for the machine's wash cycle only. Can accept a single integer from 1-9 minutes and is input on the hardware.
  
  - `WTP` : Setting the wash type for the machine cycle. Values assigned for the wash type are -
             
             1: WASH 
             0: DRAIN
  - `TMP` : Setting the temperature of the water used in washing. Values assigned for temperature are -
  
             0 : COLD
             1 : MILD
             2 : WARM
             3 : HOT        
  - `SSP` : Setting the spin speed for the wash cycle of clothes. Values assigned to the spin speed are -
  
             0 : SLOW
             1 : NORMAL
             2 : FAST

- **Reserved Locations** : Some locations have been reserved in the main memory of our system to store the parameters of the execution of our sub-routines. We actually require five memory locations for the sub-routines to execute completely. These memory locations should **always be present as labels at the end of your code**
  - `hex0000` : Stores the timer value that is input by the user. Label name - `TM`
  - `hex0001` : Stores the temperature type input by the user. Label name - `TP`
  - `hex0002` : Stores the spin speed type input by the user. Label name - `SPD`
  - `hex0003` : Stores the wash type input by the user. Label name - `WT`
  - `hex0004` : A constant value that stores the amount of time required by machine to drain and dry clothes. Label name - `CLN`



