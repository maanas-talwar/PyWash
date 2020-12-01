pywash
=============
Two Pass Assembler for a Washing Machine System

## Description
Washing machine is a simple system whose operations can be emulated through software. The assembler assumes that the operations happening on the hardware level are implemented in the system itself. The assembler only converts the assembly level program to a binary output.
- The washing machine is a simple device consisting of two basic operations - **WASH** and **DRY**.
- All the instructions, sub-routines and operations are a part of the machine that facilitate the two basic operations.
- The system consists of a **timer** to control how long a task is executed, **temperature control** to decide the temperature during the wash cycle, **spin speed** and **wash type control** to decide machine's current state i.e. washing state or drying state.
- The **timer**, **temperature control**, **spin speed** and **wash type control** are all controlled by sub-routines which implement the above descirbed operations utilizing some reserved memory locations, predefined labels and values.

For technical problems, please report to [issues](https://github.com/maanas-talwar/CAOproject/issues)  
For information regarding the sytax of the assembly level program and further insight, please refer to the [project report](https://docs.google.com/document/d/1TdVdbe3Mtm1unn6rAJ7N5usXUpmf34xankx5qu75fZo/edit?usp=sharing)

## Language:
> Python(3.8)

## Contents
```
.
└── assembler
    ├── hardcode.py
    ├── mandatorySBR.txt
    ├── Pass.py
    ├── sample_bin.txt
    ├── sample.txt
    └── wash_assemble.py
```

## Execution
* To run the assembler, first change your directory to `CAOproject/assembler/` using the following command:
> cd CAOproject/assembler/
* Save the assembly level program in this directory.
* The process can be run by the following command:
> python wash_assemble.py
* The output binary file named <program_name>_bin.txt can be found in the same directory.
