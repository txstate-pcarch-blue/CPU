# MIPS-CPU

A basic implementation of a simplified MIPS CPU with pipelining. Built using verilog and python.

## System Requirements

In order to build and run the project the computer needs to be running Linux with the following programs installed:
* iverilog
* Python3.[4-6]
* Python library myhdl version 10
* A built myhdl.vpi (See below for building instructions)

## Installing Python myhdl
Run the following commands to build the myhdl library:
> sudo apt-get install python3-pip
> sudo pip3 install myhdl

## Building and installing myhdl.vpi
myhdl is the python library we are using to connect the verilog code to the python code. It requires a compiled component to connect to the verilog model.
Running ./buildmyhdl.sh will automatically download, build, and copy myhdl.vpi to the bin directory.

## Running the cosimulation
The cosimulation is compiled and run through a single command "python3 CPU_Cosim.py <instruction_file.hex>". This will launch the cosimulation with a command line prompt that accepts the following commands:
* run <n>: Runs the simulation for n ticks. There are 20 ticks per clock cycle.
* show: Prints out both register files and tests for equality.
* quit: Exits the program, terminating the simulation.
