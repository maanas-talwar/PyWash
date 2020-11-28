# Two-Pass Assembler for a Washing Machine System - Computer Organization(CEECC07)

This is a project which aims to build a **Two-Pass Assembler for a real world system.**

### Team Members

- Maanas Talwar - Roll No: 2019UCO1544
- Anav Chaudhary - Roll No: 2019UCO1577
- Aryaman Sharma - Roll No: 2019UCO1508
- Harshit Gupta - Roll No: 2019UCO1580

## Objective

- To create a two-pass assembler for a washing machine system which produces a binary output for a task to be executed on it.
- Washing machine is a simple system whose operations can be emulated through software. In our assembler, it is asumed that the operations happening on the hardware level are implemented in the system itself and what we provide is a binary translated output of the provided assembly level program.

## Installation and Usage

1. Prerequisites - _python3, git bash(optional)_

2. Download the `wash_assemble.py` to a directory where you wish to store your assembly programs or you can run `git clone https://github.com/TheGupta2012/CAOproject.git` if you have git CLI installed in your system and `cd CAOproject` after the cloning process is done.

3. Open a terminal(linux/macOS) /command prompt(Windows) and navigate to the directory in which you downloaded the `wash_assemble.py` file.

4. It is advised to write or save your assembly program in the same directory as your `wash_assemble.py` file. An assembly file can have any extension which is (.txt or .asm). While writing any assembly program for the current assembler configuration, the code written in **SBR_memory_locs.txt** must be included before the `STP` instruction.

5. Run the assembler program by typing ``python ./wash_assemble.py``

6. After the execution of the above command, you will be prompted to type in the name your assembly file. NOTE - please provide the exact path if the file is not in the smae directory as the assembler code.

7. If the assembly code is valid, you should see a message `SUCCESSFULLY CONVERTED filename TO filename_binary.bin` and a file with the name `filename_binary.bin` should be available for you to see in the same directory as the assembler file.

8. If there are any kinds of errors or warnings(discussed later) encountered during the assembling process, the CLI would show a `ERROR ENCOUNTERED WHILE ASSEMBLING filename.asm. Please check message_filename.log for details.` message. This means that whatever errors or warnings were encountered in the building of the binary file are recorder in the .log file with time stamping and line detection.

## Structure of our System

- Our washing machine is a simple device consisting of two basic operations - **WASH** and **DRY**.

- All the instructions, sub-routines and operations are a part of the machine that facilitate the two basic operations.

- Our system consists of a **timer** which controls how long a task has to be executed, **temperature control** which decides at which temperature the wash cycle operates, **spin speed** defines the speed at which the clothes are spun in the machine and **wash type control** which decides whether the machine is in washing phase or the drying phase.

- The **timer**, **temperature control**, **spin speed** and **wash type control** are all controlled by sub-routines which implement the above descirbed operations, with some reserved memory locations, predefined labels and predefined values which correspond to a particular state of _temperature, spin speed and wash type_. The details of them are described further in the ISA of the machine.

## Instruction Set Architecture(ISA), Sub-routines and Reserved locations

### ISA

- `16-bit architecture` has been chosen for our instructions and a `12-bit , word addressable memory` is used for the storage of our instructions and operands.

<img src= "https://github.com/TheGupta2012/CAOproject/blob/main/READMEdata/instruction_format.JPG" width = 400px>

- The instructions used in our system are preceded by an addresssing mode bit which specifies _indirect_ or _direct_ addressing for our memory

- The instructions available are divided into three parts - _Register Reference, Memory Reference and Input Output_ instructions

- The system has all the basic instructions that are required in any kind of processing unit and contains the registers which are mentioned below. A point to note is that there exists a special STATUS REGISTER which actually tells the system what it is doing at the moment.

  - `AC` - Accumulator - 16bit
  - `DR` - Data register - 16bit
  - `PC` - Program counter - 12bit
  - `AR` - Adress register - 12bit
  - `INPR` - Input Register - 8bit
  - `OUTR` - Output Register - 8bit
  - `SR` - Status register - 8bit (extra bits provided for future changes in functionality)  
     <img src = "https://github.com/TheGupta2012/CAOproject/blob/main/READMEdata/status_register.JPG" width = 400px>

- **Instruction Set** : The instructions are based on the _Single Address Instruction_ format and has the accumulator as the general purpose register. X referred to in the instructions is either a memory location or a symbolic address present as a label in the program.
- Memeory Reference Instructions
  |Instruction Symbol|Hexadecimal Code (I=0)|Hexadecimal Code (I=1)|Description|
  | :-: | :-: | :-: | --- |
  |`STA X`|0XXX|8XXX|Store value of AC directly in X or the location whose address is stored in X.|
  |`LDA X`|1XXX|9XXX|Load the value of X directly or indirectly into AC.|
  |`ISZ X`|2XXX|AXXX|Increment X and the skip the next instruction if X is zero|
  |`BSA X`|3XXX|BXXX|Save return address in X and branch to the effective address of the subroutine.|
  |`BUN X`|4XXX|CXXX|Branch unconditionally to X|

  - Register Reference Instructions
    |Instruction Symbol|Hexadecimal Code|Description|
    | :-: | :-: | --- |
    |`SRT`|7800| Start the execution of the machine , takes no operands|
    |`STP`|7400| Stop the execution of the machine , takes no operands|
    |`SPN`|7200| Spinning the motor of the machine before a wash cycle(sets motor flag to 1), takes no operands|
    |`HLT`|7100| Halt motor (sets motor flag to 0), takes no operands |
    |`LCK`|7000| Lock the door of the washing machine(set a flag), takes no operands|
    |`ICL`|7080| Clear inlet flag( inlet valve closed) , takes no operands|
    |`IST`|7040| Set inlet flag ( inlet valve open) , takes no operands|
    |`OCL`|7020| Clear outlet flag ( outlet valve closed) , takes no operands|
    |`OST`|7010| Set outlet flag ( outlet valve open) and start draining , takes no operands|
    |`CLA`|7008| Clear AC , takes no operands|
    |`CMA`|7004| Complement AC , takes no operands|
    |`INC`|7002| Increment AC , takes no operands |
    |`SZA`|7001| Skip next instruction if AC is zero , takes no operands|

  - Input Output Instructions
    |Instruction Symbol|Hexadecimal Code|Description|
    | :-: | :-: | --- |
    |`SKI`|F800| Skip if input flag is set , takes no operands|
    |`INP`|F400| Input 8 bit information and clear input flag , takes no operands|
  - **_PSEUDO INSTRUCTIONS_**
    - `HEX N` : Hexadecimal number N to be converted to binary
    - `DEC N` : Signed decimal number N to be converted to binary

- **Sub-Routines** : The sub-routines for the **timing , wash-type, temperature and spin speed** are presented in this section. Note that these sub-routines refer to some predefined memory locations which are mentioned in the _Reserved Locations_ section. We are presenting the software implementations of a program for a washing-machine cycle and thus the values associated with the different settings are input through _external switches_ which indeed have representations of the values provided. The character input by the user is actually transferred in the `INPR` and then to the required memory locations in the internal executions of these subroutines.

  - `TIM` : Setting the timer for the machine's wash cycle only. Can accept a single integer from 1-9 minutes and is input on the hardware.

  - `WTP` : Setting the wash type for the machine cycle. Values assigned for the wash type are -
      
     0: WASH
    1: DRAIN
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

## Syntax

### General

- Any kind of _variable or symbolic address_ referred to in the following lines is enclosed in `[]` and all _comments_ are preceded by `;`. Instruction code are written as they are.

- Each **line of code** consists of three parts or _fields_ - _label_, _instruction_ and _comment_. Each line of code is terminated by a **new line**.

- **START MACHINE (SRT)** : Every program that is written should start with `SRT` operation which denotes the **start of execution** of the machine. Note that it is mandatory to include `SRT` at the beginning of every program you write and a program missing it would generate an **error**.

- **COMMENTS(;)** : Your program may include _comments_ inside the program which are preceded by a `;` sign. The assembler ignores any and all text present after it encounters `;` in a line. Example -

```
    ;This is a comment
    LDA [hex 2000] ;this is a line of code
```

- **STOP MACHINE(STP)** : Every program must contain an `STP` instruction at the end of the assembly program. It is a mandatory instruction to be included in the program and an **error** occurs if it is not found. However, lines of code maybe present even after the `STP` instruction so as to define symbols. Example -

```
  1. ... ; Program
     STP
  2. ... ; Program
     STP
     A, hex 1000
     B, hex 2000
```

### Opcodes, Operands and Addressing

- All the opcodes and operands are separated by one or more spaces. All the operands are _case sensitive_ while opcodes are not.

- The _Memory Reference Instructions_ occupy 2 or three symbols separated by spaces. First must be a **3 - letter symbol** defining an _MRI_. Second is a symbolic adress. The third symbol,which may or may not be present, is the letter _I_, after the operand field, to denote **indirect addressing**. Direct Addressing is assumed for any MRI instruction not ending in _I_.

- Any _Non-MRI_ must only contain a **3 - letter symbol** specifying one of the valid _Non-MRI_ as given above.

- Every line should be terminated by pressing enter or by a comment field which is in turn terminated by a new line at the end.

#### Syntax

`opcode [operand_name] [I]`

#### Examples

```
LDA and lda are same opcodes.
Var, VAR, var are different operands
CLA       ; non-MRI
LDA var I ; Indirect Addressing MRI
LDA var   ; Direct Addressing MRI
```

### Symbolic addresses and Labels

- There are certain rules defined for the declaration of the symbolic addresses and labels in your program. They are -
  1. It can not contain spaces
  2. It may not start with a numeric value
  3. It can start with and contain only Alpha-numeric characters and `_`
  4. It can not be same as a predefined label, sub-routine or opcode
  5. It can not be the same as an already declared symbol / label
  6. It must contain **at most 3 characters**

#### Valid symbolic addresses and labels

```
VAR
a
AB_
t1
```

#### Invalid symbolic addresses and labels

```
2va      ; starts with a numeric value
t.v      ; contains "." character
m v      ; contains a space in the declaration
SPN/spn  ; same as a predefined instrcution
name     ; contains more than 3 letters
```

#### Syntax for labels

- The label name must be followed by a ":" immediately after the label name and the code associated with the label may start from the same line,separated by one or more spaces, or from the next line.
- If the label defines an operand, it must be followed by a "," without a space. The value associated with the symbol must be defined in the same line after the ",".

```
[LABEL_NAME]: additional code
[LABEL_NAME], value
```

### Example

- Please click [here](https://github.com/TheGupta2012/CAOproject/blob/main/sample.txt) to see an example program written according to the rules provided.

### Errors

- The following rules have to be taken care of while writing a program for the execution of a washing machine assembly program. They are -
  - Every program must contain an `SRT` (START) instruction as the first instruction. Failure to do so would result in a **fatal error** and the execution of the assembler would not be initiated.
  - Each and every line must be terminated by a **new line**. Not doing so results in a syntax error.
  - Each line of code must contain atmost three _fields_ that are label, instruction, comments. A line of code conatining any more fields is considered as an error.
  - Each symbolic address that is mentioned in any instruction field must occur again as a label field. If not found, an error is generated.
  - No symbolic address or label must be same as a predefined opcode, sub-routine or label field. If a same name is found, an error is generated.
  - All the _Memory Reference Instructions_ must contain an operand or a constant value. Failure to detect an operand in an _MRI_ produces an error.
  - All the _Non- Memory Reference Instructions_ must not contain any operand value. An error is generated if the assembler detects an operand.

## Running the Assembler

 - Clone the repository in your system using `git clone` with `repository_link.git` If you do not have `git` installed in your system, you can simply download the codes present in `assembler` folder in our repository.
 
 - With the assembler code downloaded, open `cmd` and navigate to the directory in which your code resides. ( If you used `git clone` just type `cd CAOproject/assembler`). See below - 
 
 <img src = "https://github.com/TheGupta2012/CAOproject/blob/main/READMEdata/step1.JPG" width = 400px >
 
- Save the file, conatining your assembly program, in the `assembler` folder or the same directory in which your assembler codes reside in. NOTE - all the file in the `assembler` directory need to be present in the same folder.

   <img src = "https://github.com/TheGupta2012/CAOproject/blob/main/READMEdata/step2.JPG" width = 400px >
 
- Run the code by typing `python wash_assemble.py` on the terminal and you would see a prompt message asking the name for your file. Type in the name and press enter. You should see the assembler starting and a syntax check.

- If your code is error free, the two passes of the assembler should initiate and a final binary output would be generated in the same folder with the name `filename_bin.txt`
  - **SUCCESSFUL EXECUTION** - [CODE](https://github.com/TheGupta2012/CAOproject/blob/main/assembler/sample.txt)
  
  
   <img src = "https://github.com/TheGupta2012/CAOproject/blob/main/READMEdata/success.JPG" width = 400px >
  
  - **ERRONEUS EXECUTION** - [CODE](https://github.com/TheGupta2012/CAOproject/blob/main/assembler/error_program.txt)
  

   <img src = "https://github.com/TheGupta2012/CAOproject/blob/main/READMEdata/fail.JPG" width = 400px >
