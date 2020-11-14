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












