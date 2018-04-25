# MIPS-CPU

A basic implementation of a simplified MIPS CPU with pipelining. Built using verilog and python.

## System Requirements

In order to build and run the project the computer needs to be running Linux with the following programs installed:
* iverilog
* Python3 versions 3.4 through 3.6 (myhdl doesn't work with 3.7 and above)
* Python library myhdl version 10
* A built myhdl.vpi (See below for building instructions)

## Getting the Cosimulation to Run on Windows

As the cosimulation depends on the behavior of Linux, it is impossible to run the cosimulation directly on Windows.
Luckily, a workaround is available in the "[Windows Subsystem For Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)".
The link will walk you through the installation. Note that this only works for Windows 10.

Trying to use the cygwin/mingw toolkit will not work as the OS features are not emulated.

## Installing Python myhdl
Run the following commands to build the myhdl library:
```
sudo apt-get install python3-pip
sudo pip3 install myhdl
```

## Building and installing myhdl.vpi
myhdl is the python library we are using to connect the verilog code to the python code. It requires a compiled component to connect to the verilog model.
Running ./buildmyhdl.sh will automatically download, build, and copy myhdl.vpi to the bin directory.

## Generating an input file

### Random Generation
Input files can be generated with random instructions via the tools/Generator.py program.
This generation is configured through editing the tools/gen.conf file. These are the changable parameters:

* "i_count: n" sets the number of generated instructions to be n.
* "pf_p: f" sets the percentage of program flow assignments, f must be in [0:1]
* "mem_p: f" sets the percentage of memory access functions, f must be in [0:1]

ALU operations are supplied to fill in all operations that are not program flow or memory operations.

The generator can be called with:

```
cd tools
python3 Generator output.hex
```

### Using the assembler

The tools/Assembler.py python programs works if you already have a given program's source code. Note that there is only .text generation and no .data.

The assembler can be called with:

```
cd tools
python3 Assembler.py [-o out_file] infile.S
```

## Input File Requirements

Input files must be ASCII representations of hex digits separated by a new line character. Example:

```
20100004
20110004
2012ffff
...
```

## Running the cosimulation
The cosimulation is compiled and run through the CPU_Cosim.py file using the command:
```
python3 CPU_Cosim.py input.hex
```

This will launch the cosimulation with a command line prompt that accepts the following commands:
* run <n>: Runs the simulation for n ticks. There are 20 ticks per clock cycle.
* show: Prints out both register files and tests for equality.
* quit: Exits the program, terminating the simulation.

## Project Structure
### Folder Conventions
Files are stored in this tree structure as follows:

```
.
├── bin             Stores compiled files
├── lib             Stores external libraries
│   └── myhdl           myhdl libary, used to compile myhdl.vpi
├── python          Stores python simulation files
│   └── helpers         Stores python test bench helping functions
├── samples         Stores sample code for simulation testing
├── tools           Stores assembler and generator files
└── verilog         Stores verilog simulation files
```

### File Conventions

All verilog files end with `.v` and all python files end with `.py`

If a file end with `_tb.[py|v]`, then the file is used to test the module.

If a file end with `_cosim.[py|v]`, then the file is used to control cosimulation. Each `_cosim.[py|v]` pair is used to control one build target. I.E. the Register_File_cosim files are not used in the CPU Cosimulation. Run the python files to initiate cosimulation.

## Credits

This program was built by the Texas State PC Architecture Blue Team.

**Team Lead:** Michael Volling

**Verilog Team**

* Boris Sabotinov **Lead**
* Daniel Le
* Cody Sears

**Python Team**
* Kevin Maxey **Lead**
* Matthew Maluschka
* Erich McLaurin
